import logging
import os
import tweepy

logger = logging.getLogger()

class Tweeter:
    def __init__(self):
        self.api = self.create_api()
    
    def create_api(self):
        # consumer_key = os.getenv("CONSUMER_KEY")
        # consumer_secret = os.getenv("CONSUMER_SECRET")
        # access_token = os.getenv("ACCESS_TOKEN")
        # access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

        consumer_key = "iXPbyy6NaLZBV2FsTTxIim1Rh"
        consumer_secret = "8y75G13x55gdh3ZD5GWPpoSOPfDi9mwN0qgH2mpQwhTVaWw6PM"
        access_token = "4888449014-pvfbzz0MfeUKbZLJGNRygFSADlLNPK7ssYIpK3l"
        access_token_secret = "2qC7Eq2eKMtL6tCq4EkLrmzw4GxM6tiq3ca59yxcDFVXe"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        try:
            api.verify_credentials()
        except Exception as e:
            logger.error("Error creating API", exc_info=True)
            raise e
        logger.info("API created")
        return api

    def tweet(self, msg):
        self.api.update_status(msg)
        # for now just write to file
        with open('updates.txt', 'w') as f:
            f.write(msg)