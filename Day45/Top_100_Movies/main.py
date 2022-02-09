import requests
from bs4 import BeautifulSoup


TOP_MOVIES = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'


with requests.Session() as session:
    response = session.get(TOP_MOVIES)

site_content = response.text
soup = BeautifulSoup(site_content, 'html.parser')
movies = soup.find_all(name='h3', class_='title')

top_100 = [movie.getText() for movie in movies]
top_100.reverse()

with open('Day45/Top_100_Movies/movies.txt', mode='w') as file:
    for movie in top_100:
        file.write(f'{movie}\n')
