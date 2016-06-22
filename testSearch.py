import got
import tweetdb
import time
from sentiment import SentimentParser

# print "Going to search tweets..."
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch('captain america civil war').setSince("2016-03-01").setUntil("2016-06-20").setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet("test-civil-war", tweet, parser.parse(tweet.text))
# print "Done..."


tweetdb.readAllTweets("test-civil-war")