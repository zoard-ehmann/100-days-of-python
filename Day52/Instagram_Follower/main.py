import os

from dotenv import load_dotenv
from insta_follower import InstaFollower


load_dotenv()

INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_UN')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PW')
SIMILAR_ACCOUNT = os.getenv('ACCOUNT_TO_FOLLOW')


insta_follower = InstaFollower()

insta_follower.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
