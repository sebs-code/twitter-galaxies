import tweepy
import time
import random
import decimal
import json

from constants import BEARER_TOKEN, CATEGORIES


def get_followers(twitter_handle):
    """
    Scrapes a list of followers from a Twitter account.
    """

    auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
    api = tweepy.API(auth)

    list = open('data/followers.txt', 'w')

    if (api.verify_credentials):
        print('We successfully logged in')

    user = tweepy.Cursor(api.get_followers()).items()

    while True:
        try:
            u = next(user)
            list.write(u.screen_name + ' \n')

        except:
            time.sleep(15 * 60)
            print('We got a timeout ... Sleeping for 15 minutes')
            u = next(user)
            list.write(u.screen_name + ' \n')
    list.close()


def generate_data():
    """
    Generates a dummy data set for all categories, for all followers pulled
    in the FOLLOWERS.txt file
    """

    data = []

    with open('data/followers.txt') as followers:
        for follower in followers:
            entry = {"username": str(follower).strip()}
            for category in CATEGORIES:
                entry[category] = float(decimal.Decimal(random.randrange(-100, 100))/100)

            data.append(entry)
        print(data)

    with open('data/data.json', 'w') as f:
        json.dump(data, f)
