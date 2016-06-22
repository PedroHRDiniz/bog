from pymongo import MongoClient
from sentiment import SentimentParser
import got

def insertTweet(collection, tweet, sentiment):
    client = MongoClient()
    db = client.taia
    
    key = { "_id": tweet.id}
    data = {
        "permalink": tweet.permalink,
        "username": tweet.username,
        "text": tweet.text,
        "date": tweet.date,
        "retweets": tweet.retweets,
        "favorites": tweet.favorites,
        "mentions": tweet.mentions,
        "hashtags": tweet.hashtags,
        "geo": tweet.geo,
        "sentiment": sentiment,
    }
    db[collection].update_one(key, {"$set": data}, upsert=True) 

def readAllTweets(collection):
    client = MongoClient()
    db = client.taia
    cursor = db[collection].find()
    for tweet in cursor:
        print u'{0}: {1}'.format(tweet["text"], tweet["sentiment"])