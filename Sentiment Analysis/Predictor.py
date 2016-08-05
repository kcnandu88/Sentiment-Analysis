'''
Created on Jul 23, 2015

@author: Nandu
'''
 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline, make_union
 
from Piping import Dictionary
from Piping.Dictionary import PosNeg
from Transformation import ExtractText


def target(phrases):
    
    return [datapoint.sentiment for datapoint in phrases]

class Prediction:

    def __init__(self, lowercase=True,
                 binary=False,
                 min_df=0, ngram=1, stopwords=None, limit_train=None,
                 map_to_lex=True, duplicates=False):
        
        pipeline = [ExtractText(lowercase)]
        
        ext = [build_text_extraction(binary=binary, min_df=min_df,
                                     ngram=ngram, stopwords=stopwords)]
         
        ext.append(build_lex_extraction(binary=binary, min_df=min_df,
                                            ngram=ngram))

        ext = make_union(*ext)
        pipeline.append(ext)
        classifier = KNeighborsClassifier()

        self.pipeline = make_pipeline(*pipeline)
        self.classifier = classifier

    def fit(self, phrases, y=None):
        y = target(phrases)
        Z = self.pipeline.fit_transform(phrases, y)
        self.classifier.fit(Z, y)
        return self
    
    def predict(self, phrases):
        Z = self.pipeline.transform(phrases)
        labels = self.classifier.predict(Z)
        return labels  
      
def build_text_extraction(binary, min_df, ngram, stopwords):
    return make_pipeline(CountVectorizer(binary=binary,
                                         tokenizer=lambda x: x.split(),
                                         min_df=min_df,
                                         ngram_range=(1, ngram),
                                         stop_words=stopwords))
def build_lex_extraction(binary, min_df, ngram):
    return make_pipeline(PosNeg(), CountVectorizer(binary=binary,
                                         tokenizer=lambda x: x.split(),
                                         min_df=min_df,
                                         ngram_range=(1, ngram)))    
    
    
