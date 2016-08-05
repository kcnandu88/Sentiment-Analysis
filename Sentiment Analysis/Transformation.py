'''
Created on Jul 23, 2015

@author: Nandu
'''
import nltk

class ExtractText:

    def __init__(self, lowercase=False):
        self.lowercase = lowercase

    def transform(self, X):
        
        it = (" ".join(nltk.word_tokenize(datapoint.long_comment)) for datapoint in X)
        if self.lowercase:
            return [x.lower() for x in it]
        return list(it)
    
    def fit(self, X, y=None):
        return self
    
