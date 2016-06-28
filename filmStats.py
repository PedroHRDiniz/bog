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
    score3 = float(0)
    score4 = float(0)
    score5 = float(0)
    score6 = float(0)
    score7 = float(0)
    score8 = float(0)
    client = MongoClient()
    db = client.taia
    film_stats = db["filmstats"].find_one({"name": film})
    
    cursor = db[film].find()
    for tweet in cursor:
        if(tweet["sentiment"]["neu"] < 0.7):
            rt = ((1 + tweet["retweets"])/float(film_stats["qtRT"] + film_stats["qtTweets"]))
            fav = ((1 + tweet["favorites"])/float(film_stats["qtFav"] + film_stats["qtTweets"]))
            score_rt_v = tweet["sentiment"]["compound"] * rt
            score += score_rt_v
            score2 += tweet["sentiment"]["compound"]
            score_fav_v = tweet["sentiment"]["compound"] * fav
            score3 += score_fav_v
            score4 += (score_rt_v*0.7 + score_fav_v*0.3)
            score_rt_k = tweet["score"] * rt
            score5 += score_rt_k
            score6 += tweet["score"]
            score_fav_k = tweet["score"] * fav
            score7 += score_fav_k
            score8 += (score_rt_k*0.7 + score_fav_k*0.3)
    score2 = score2 / film_stats["qtTweets"]
    score6 = score6 / film_stats["qtTweets"]
    
    #print "score 1:", film, score
    #print "score 2:", film, score2
    #print "score 3:", film, score3
    print "score 4:", film, score4
    #print "score 5:", film, score5
    #print "score 6:", film, score6
    #print "score 7:", film, score7
    #print "score 8:", film, score8
    data = {
        "score": score,
        "score2": score2,
        "score3": score3,
        "score4": score4,
        "score5": score5,
        "score6": score6,
        "score7": score7,
        "score8": score8,
    }
    #score = score/film_stats["qtTweets"]
    #print film, score
    db["filmstats"].update_one({"name": film}, {"$set": data}, upsert=True) 
    return score