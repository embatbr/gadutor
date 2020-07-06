# -*- coding: utf-8 -*-

import logging
import os

import tweepy


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


MY_NAME = 'gadutor'
MENTION_ME = f'@{MY_NAME}'


def create_api():
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    try:
        api = tweepy.API(
            auth,
            wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True
        )

        api.verify_credentials()

        logger.info("API created")
        return api
    except Exception as err:
        logger.error("Error creating API", exc_info=True)
        raise err
