import logging
import os
import tweepy

logger = logging.getLogger()

class Util():
    def __init__(self):
        self.api = self.create_api()
    
    def create_api(self):
        consumer_key = os.getenv("CONSUMER_KEY")
        consumer_secret = os.getenv("CONSUMER_SECRET")
        access_token = os.getenv("ACCESS_TOKEN")
        access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        try:
            api.verify_credentials()
        except Exception as e:
            logger.error("Error creating API", exc_info=True)
            raise e
        logger.info("API created")
        return api

    def tweet(self, msg):
        self.api.update_status(msg)
        
        with open('updates.txt', 'w') as f:
            f.write(msg)

    