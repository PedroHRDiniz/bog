import got
import tweetdb
import filmStats

def main():
	
	def printTweet(descr, t):
		print descr
		print "Username: %s" % t.username
		print "Retweets: %d" % t.retweets
		print "Text: %s" % t.text
		print "Mentions: %s" % t.mentions
		print "Hashtags: %s\n" % t.hashtags
	'''
	# Example 1 - Get tweets by username
	tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
	
	printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)
	
	# Example 2 - Get tweets by query search
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(1)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
	
	printTweet("### Example 2 - Get tweets by query search [europe refugees]", tweet)
	
	# Example 3 - Get tweets by username and bound dates
	tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
	
	printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)
	
	#tweetdb.readAllTweets("deadpool")
	
	filmStats.calc_info("deadpool")
	filmStats.calc_info("kung fu panda 3")
	filmStats.calc_info("the martian")
	filmStats.calc_info("mockingjay")
	filmStats.calc_info("kingsman")
	filmStats.calc_info("fifty shades of grey")
	filmStats.calc_info("ex machina")
	filmStats.calc_info("inside out")
	filmStats.calc_info("jurassic world")
	filmStats.calc_info("force awakens")
	filmStats.calc_info("hateful eight")
	filmStats.calc_info("finest hours")
	filmStats.calc_info("gods of egypt")
	'''
	#filmStats.calc_info("zoolander 2")
	
	filmStats.calc_score("deadpool")
	filmStats.calc_score("kung fu panda 3")
	filmStats.calc_score("the martian")
	filmStats.calc_score("mockingjay")
	filmStats.calc_score("kingsman")
	filmStats.calc_score("fifty shades of grey")
	filmStats.calc_score("ex machina")
	filmStats.calc_score("inside out")
	filmStats.calc_score("jurassic world")
	filmStats.calc_score("force awakens")
	filmStats.calc_score("hateful eight")
	filmStats.calc_score("finest hours")
	filmStats.calc_score("gods of egypt")
	filmStats.calc_score("zoolander 2")
if __name__ == '__main__':
	main()
	