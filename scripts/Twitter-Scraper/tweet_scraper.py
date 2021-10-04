"""Scrape Tweets of a Hashtag using Twitter API"""

import twitter_credentials
import tweepy
import csv
import pandas as pd
import os

dir = "outputs"
if not os.path.exists(dir):
    os.mkdir(dir)


def search_for_hashtags(
    api_key, api_secret_key, access_token, access_token_secret, hashtag_phrase
):

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    data = []
    for tweet in tweepy.Cursor(
        api.search_tweets,
        q=hashtag_phrase + " -filter:retweets",
        lang="en",
        tweet_mode="extended",
    ).items(100):
        rowData = [
            tweet.created_at,
            tweet.full_text.replace("\n", " ").encode("utf8"),
            tweet.user.screen_name.encode("utf8"),
            [e["text"] for e in tweet._json["entities"]["hashtags"]],
            tweet.user.followers_count,
        ]
        data.append(rowData)

    df = pd.DataFrame(
        data,
        columns=[
            "timestamp",
            "tweet_text",
            "username",
            "all_hashtags",
            "followers_count",
        ],
    )
    df.to_csv(f"outputs\\{hashtag_phrase}.csv", index=False)


consumer_key = twitter_credentials.API_key.encode("utf-8")
consumer_secret = twitter_credentials.API_secret_key.encode("utf-8")
access_token = twitter_credentials.Access_token.encode("utf-8")
access_token_secret = twitter_credentials.Access_token_secret.encode("utf-8")

hashtag_phrase = input("Hashtag Phrase: ")

search_for_hashtags(
    consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase
)
