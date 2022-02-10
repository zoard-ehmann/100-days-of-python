import os
import pprint

import requests
import spotipy
from song import Song
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv


load_dotenv()

SPOTIPY_CID = os.getenv('SPOTIFY_CID')
SPOTIFY_SECRET = os.getenv('SPOTIFY_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100'


def format_text(text: BeautifulSoup) -> str:
    """Takes a BeautifulSoup object and returns the stripped inner text.

    Args:
        text (BeautifulSoup): BeautifulSoup object with HTML tags.

    Returns:
        [type]: Stripped inner text of the passed in HTML.
    """
    return text.getText().strip('\n')


# Initialization
pp = pprint.PrettyPrinter(indent=4)
date = input('What year would you like to travel? YYYY-MM-DD: ')

# Get the Billboard HTML and create a BS object from it
with requests.Session() as billboard_conn:
    response = billboard_conn.get(f'{BILLBOARD_URL}/{date}')
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

# Get all the rows which contains the relevant information about the title and artist
billboard = soup.select(selector='.o-chart-results-list-row-container .o-chart-results-list-row')

# Create and collect song objects with title and artist from all the billboard rows
songs = []
for song in billboard:
    soup = BeautifulSoup(str(song), 'html.parser')
    title = format_text(soup.find(name='h3', class_='c-title'))
    artist = format_text(soup.select_one(selector='.lrv-u-width-100p .c-label'))
    songs.append(Song(artist=artist, title=title))

# Authenticate with Spotify and get the user ID
spotify_scope = ['playlist-modify-private']
spotify_auth = SpotifyOAuth(
    client_id=SPOTIPY_CID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    cache_path='Day46/Music_Time_Machine/.cache',
    scope=spotify_scope
)
spotify_client = spotipy.Spotify(auth_manager=spotify_auth)
spotify_uid = spotify_client.current_user()['id']

# Collect the tracks from Spotify
new_playlist = []
for song in songs:
    # Check if there's an exact match with the artist / song title
    response = spotify_client.search(q=f'track:{song.title} artist:{song.artist}', limit=1)
    # Use the specified year instead of the artist if no match
    if len(response['tracks']['items']) == 0:
        response = spotify_client.search(q=f'track:{song.title} year:{date.split("-")[0]}', limit=1)
    # Append the track to the playlist only if song can be found on Spotify
    try:
        track_id = response['tracks']['items'][0]['id']
    except IndexError:
        print(f'{song.title} from {song.artist} not found on Spotify, skipping from the playlist.')
    else:
        new_playlist.append(track_id)

# Create a new playlist on Spotify
playlist_info = spotify_client.user_playlist_create(user=spotify_uid, name=f'{date} Billboard 100', public=False, description=f'Top tracks of {date}.')
playlist_id = playlist_info['id']

# Add the tracks to the newly created playlist
spotify_client.playlist_add_items(playlist_id=playlist_id, items=new_playlist)