import fcntl
import sys
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from collections import defaultdict
import os.path
count = 0
 
def word_feats(words):
    return dict([(word, True) for word in words])
 
def word_feats_sentence(sentence):
	return word_feats(sentence.split(' '))

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4

trainfeats = negfeats + posfeats 
#trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
#testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
#print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
classifier = NaiveBayesClassifier.train(trainfeats)
#print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
#classifier.show_most_informative_features()
while True:	
	filename = str(count) + ".txt"
	while not os.path.isfile(filename):
		continue
	f = open(filename,'r')
	dictionary_tweets = defaultdict(lambda:[0,0])
	#for sentence in f:
	#	print sentence + " " + classifier.classify(word_feats_sentence(sentence))
	fp = open("sentiment_" + str(count) + ".txt", "w")
	tweet_count = 0
	for line in f:
		word_parts = line.split("#")
		sentiment = classifier.classify(word_feats_sentence(line))
		if (sentiment == "pos"):
			sentiment = 0
		else:
			sentiment = 1
		hash_words = []
		for part in word_parts:
			if len(part) > 0:
				# print part.split()
				hash_word = part.split(' ')[0].lower()
				dictionary_tweets[hash_word][sentiment] = dictionary_tweets[hash_word][sentiment] + 1
			
	for i in dictionary_tweets:
		if i.split('\n') != "":
			print >> fp, i.split('\n')[0], dictionary_tweets[i][0], dictionary_tweets[i][1]
	fp.close()
	f.close()
	count += 1