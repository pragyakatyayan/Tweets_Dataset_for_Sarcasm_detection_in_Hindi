import tweepy
import csv
import pandas as pd
import sys

####input your credentials here
consumer_key = '---'
consumer_secret = '---'
access_token = '---'
access_token_secret = '---'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('tweets.csv', 'a', encoding='UTF-8')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#irony",count=100,
                           lang="hi",
                           since="2015-06-03").items(3000):
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('UTF-8')])
