from internet_speed_twitter_bot import InternetSpeedTwitterBot


twitter_bot = InternetSpeedTwitterBot()
internet_speed = twitter_bot.get_internet_speed()

if internet_speed['up'] < twitter_bot.guaranteed_up or internet_speed['down'] < twitter_bot.guaranteed_down:
    twitter_bot.tweet_at_provider(internet_speed)

twitter_bot.close_browser()