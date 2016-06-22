#calculate quantity of RTs and favorites of all tweets from the film and update the film's stats
from pymongo import MongoClient

def calc_info(film):
    qt_rt = 0
    qt_fav = 0
    qt_tweets = 0
    score = 0
    client = MongoClient()
    db = client.taia
    cursor = db[film].find()
    
    for tweet in cursor:
        if(tweet["sentiment"]["neu"] < 0.7): 
            qt_rt += tweet["retweets"]
            qt_fav += tweet["favorites"]
            qt_tweets += 1
    
    key = {"name": film}
    data = {
        "qtRT": qt_rt,
        "qtFav": qt_fav,
        "qtTweets": qt_tweets,
        "score": score,
    }
    db["filmstats"].update_one(key, {"$set": data}, upsert=True) 
    
def calc_score(film):
    score = float(0)
    score2 = float(0)
    client = MongoClient()
    db = client.taia
    film_stats = db["filmstats"].find_one({"name": film})
    
    cursor = db[film].find()
    for tweet in cursor:
        if(tweet["sentiment"]["neu"] < 0.7):
            score += tweet["sentiment"]["compound"] * ((1 + tweet["retweets"])/float(film_stats["qtRT"] + film_stats["qtTweets"]))
            score2 += tweet["sentiment"]["compound"]
    score2 = score2 / film_stats["qtTweets"]
    print "score 1:", film, score
    print "score 2:", film, score2
    #score = score/film_stats["qtTweets"]
    #print film, score
    db["filmstats"].update_one({"name": film}, {"$set": {"score": score}}, upsert=True) 
    return score