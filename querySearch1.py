import got
import tweetdb
import time
from sentiment import SentimentParser

# movieName = "kung fu panda 3"
# dateSince = "2016-01-15"
# dateUntil = "2016-02-29"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "deadpool"
# dateSince = "2016-01-29"
# dateUntil = "2016-03-12"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "the martian"
# dateSince = "2015-09-18"
# dateUntil = "2015-11-02"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "mockingjay"
# dateSince = "2015-11-06"
# dateUntil = "2015-12-20"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "kingsman"
# dateSince = "2015-01-30"
# dateUntil = "2015-03-13"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "fifty shades of grey"
# dateSince = "2015-01-30"
# dateUntil = "2015-03-13"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "ex machina"
# dateSince = "2015-04-10"
# dateUntil = "2015-05-24"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "inside out"
# dateSince = "2015-05-05"
# dateUntil = "2015-06-19"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "jurassic world"
# dateSince = "2015-05-29"
# dateUntil = "2015-07-12"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "force awakens"
# dateSince = "2015-12-04"
# dateUntil = "2016-01-18"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "hateful eight"
# dateSince = "2015-12-16"
# dateUntil = "2016-01-30"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "finest hours"
# dateSince = "2016-01-15"
# dateUntil = "2016-02-29"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "gods of egypt"
# dateSince = "2016-02-12"
# dateUntil = "2016-03-26"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# movieName = "zoolander 2"
# dateSince = "2016-01-29"
# dateUntil = "2016-03-12"
# print "Searching tweets for " + movieName
# start = time.time()
# tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
# tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# end = time.time()
# print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

# for tweet in tweets:
#     parser = SentimentParser()
#     tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
# print "Done..."


# nope
movieName = "jack and jill"
dateSince = "2011-10-28"
dateUntil = "2011-12-11"
print "Searching tweets for " + movieName
start = time.time()
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movieName).setSince(dateSince).setUntil(dateUntil).setMaxTweets(10000)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
end = time.time()
print "Got " + str(len(tweets)) + " and it took " + str(end - start) + " seconds. Adding them to the database..."

for tweet in tweets:
    parser = SentimentParser()
    tweetdb.insertTweet(movieName, tweet, parser.parse(tweet.text))
print "Done..."