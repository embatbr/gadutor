# -*- coding: utf-8 -*-

import logging
import os
import time

import tweepy

import config


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


COMMANDS = {
    'traduzir',
    # 'gargalhar',
    # 'blockers'
}


def check_mentions(api, command, since_id, run_function):
    new_since_id = since_id

    cursor = tweepy.Cursor(api.mentions_timeline, since_id=new_since_id).items()
    for tweet in cursor:
        logger.info("Retrieving mentions")
        new_since_id = max(tweet.id, new_since_id) + 1

        text_words = tweet.text.strip().split()

        if config.MENTION_ME not in text_words:
            continue

        mention_index = text_words.index(config.MENTION_ME)
        command_index = mention_index + 1

        if len(text_words) <= command_index:
            continue
        if text_words[command_index].strip() != command:
            continue

        in_reply_to_status_id = tweet.in_reply_to_status_id
        try:
            replied_tweet = api.get_status(in_reply_to_status_id, tweet_mode='extended')
            if replied_tweet:
                text_to_reply = replied_tweet.full_text
                mu_text = run_function(text_to_reply)
                reply_text = '@{} {}'.format(replied_tweet.user.screen_name, mu_text)

                print()
                print(replied_tweet.id)
                print()
                print(text_to_reply)
                print()
                print(reply_text)
                print()
                print('-------------------')

                api.update_status(
                    status=reply_text,
                    in_reply_to_status_id=in_reply_to_status_id
                )
        except tweepy.error.TweepError as err:
            print(err)

    return new_since_id


def main(run_function):
    api = config.create_api()

    since_id = 1

    since_ctrl_filepath = '{}/since_mention'.format(config.CMD_CTRL)
    if os.path.exists(since_ctrl_filepath):
        since_id = int(open(since_ctrl_filepath).read())

    while True:
        logger.info("since_id: %s" % since_id)
        since_id = check_mentions(api, 'traduzir', since_id, run_function)

        with open(since_ctrl_filepath, 'w') as file:
            file.write(str(since_id))

        logger.info("Waiting...")
        time.sleep(60)
