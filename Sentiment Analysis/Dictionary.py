'''
Created on Jul 23, 2015

@author: Nandu
'''
from _collections import defaultdict
import csv
import os
import re

class PosNeg:
    '''
    classdocs
    '''  
    def transform(self, X, y=None):
        corpus = self._get_corpus()
        result = []
        for phrase in X:
            newphrase = []
            for word in phrase.split():
                newphrase.extend(corpus.get(word.lower(), []))
            result.append(" ".join(newphrase))
        return result
    
    def fit(self, X, y=None):
        return self
    
    def _get_corpus(self):


        dict = {}
        with open('positive.txt', 'r') as posSentences:
            for i in posSentences:
                posWords = re.findall(r"[\w']+|[.,!?;]", i.rstrip())
                for word in posWords:
                    dict[word] = 'pos'
        
        with open('negative.txt', 'r') as negSentences:
            for i in negSentences:
                negWords = re.findall(r"[\w']+|[.,!?;]", i.rstrip())
                for word in posWords:
                    dict[word] = 'neg'


        print len(dict)
        return dict
