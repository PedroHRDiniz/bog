from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import twitter_samples
import unicodedata
from pymongo import MongoClient

strings_negative = twitter_samples.strings('negative_tweets.json')
strings_positive = twitter_samples.strings('positive_tweets.json')

neg_docs = [(unicodedata.normalize('NFKD', sent).encode('ascii','ignore').split(), -1) for sent in strings_negative]
pos_docs = [(unicodedata.normalize('NFKD', sent).encode('ascii','ignore').split(), 1) for sent in strings_positive]
# print len(neg_docs), len(pos_docs)
# print neg_docs[0]

train_neg_docs = neg_docs[:5000]
train_pos_docs = pos_docs[:5000]
training_docs = train_neg_docs+train_pos_docs

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
training_set = sentim_analyzer.apply_features(training_docs)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)

'''
client = MongoClient()
db = client.taia
tweet = db["kingsman"].find()[0]
print tweet["text"]
print sentim_analyzer.classify(tweet["text"].split())
'''
def calc_score_tweets(film):
    client = MongoClient()
    db = client.taia
    cursor = db[film].find()
    print "Starting ", film
    for tweet in cursor:
        score_tweet = sentim_analyzer.classify(tweet["text"].split())
        db[film].update_one({"_id": tweet["_id"]}, {"$set": {"score": score_tweet}}, upsert=True)
    print "Finish"
#calc_score_tweets("deadpool")
#calc_score_tweets("kung fu panda 3")
#calc_score_tweets("the martian")
#calc_score_tweets("mockingjay")
#calc_score_tweets("kingsman")
#calc_score_tweets("fifty shades of grey")
#calc_score_tweets("ex machina")
#calc_score_tweets("inside out")
#calc_score_tweets("jurassic world")
#calc_score_tweets("force awakens")
#calc_score_tweets("hateful eight")
#calc_score_tweets("finest hours")
#calc_score_tweets("gods of egypt")
calc_score_tweets("zoolander 2")

'''
for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))
#Evaluating NaiveBayesClassifier results...
'''
'''
Accuracy: 0.8
F-measure [obj]: 0.8
F-measure [subj]: 0.8
Precision [obj]: 0.8
Precision [subj]: 0.8
Recall [obj]: 0.8
Recall [subj]: 0.8
'''