from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import json
import pandas as pd
import csv
import re
from textblob import TextBlob
import string
import preprocessor as p
import os
import time
import scraptweets

# Twitter credentials
# Obtain them from your twitter developer account
consumer_key = '---'
consumer_secret = '---'
access_key = '---'
access_secret = '---'
# Pass your twitter credentials to tweepy via its OAuthHandler
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Initialise these variables:
search_words = "#कटाक्ष OR #kataksh OR #sarcasm OR #sarcastic OR #irony"
date_since = "2012-01-01"
numTweets = 2500
numRuns = 10
# Call the function scraptweets
scraptweets.scraptweets(search_words, date_since, numTweets, numRuns)
