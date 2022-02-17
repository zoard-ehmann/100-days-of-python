import os

from dotenv import load_dotenv
from insta_follower import InstaFollower


load_dotenv()

INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_UN')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PW')
SIMILAR_ACCOUNT = os.getenv('ACCOUNT_TO_FOLLOW')
FIREFOX_PROFILE = os.getenv('FF_PROFILE')


insta_follower = InstaFollower(firefox_profile=FIREFOX_PROFILE)

insta_follower.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
insta_follower.find_followers(account=SIMILAR_ACCOUNT)
insta_follower.follow()
insta_follower.end_session()