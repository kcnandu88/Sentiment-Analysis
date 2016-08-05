'''
Created on Jul 14, 2015

@author: Nandu
'''
import collections
import math
import re

from nltk.classify.naivebayes import NaiveBayesClassifier
import pandas
import nltk
import pickle

class SentimentAnalysis(object):
    
    def makeadict(self,values):
        return dict([(word, True) for word in values])
    
                 
    def cal(self,values,modell):
        self.values=values
        print modell.classify(values);
    
    def finalclassification(self):
        negative_words=[]
        positive_words=[]
        with open('positive.txt', 'r') as posSentences:
            for i in posSentences:
                posWords = re.findall(r"[\w']+|[.,!?;]", i.rstrip())
                posWords = [negativevalues.makeadict(posWords), 'pos']
                positive_words.append(posWords)
        with open('negative.txt', 'r') as negSentences:
            for i in negSentences:
                negWords = re.findall(r"[\w']+|[.,!?;]", i.rstrip())
                negWords = [negativevalues.makeadict(negWords), 'neg']
                negative_words.append(negWords)

        trainFeatures = positive_words[:] + negative_words[:]


        classifier = NaiveBayesClassifier.train(trainFeatures)    
        return classifier

      
    
negativevalues=SentimentAnalysis();
modell=negativevalues.finalclassification()
test={}
words="good"
for i in words:
    test[i]=True
#negativevalues.cal(tet, modell)
print modell.classify(test)


# import pickle
# f = open('my_classifier.pickle')
# classifier = pickle.load(f)
# f.close()
