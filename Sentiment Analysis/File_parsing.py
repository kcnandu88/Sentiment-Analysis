'''
Created on Jul 23, 2015

@author: Nandu
'''
import csv
import random

from Data import SentimentTrainer 
from Predictor import Prediction


class Parser:
    '''
    classdocs
    '''
    def _iter_data_file(self,filename):

        it = csv.reader(open(filename, "r"), delimiter=",")
        row = next(it)
#         if " ".join(row[:2]) != "sentiment long_comment":
#             raise ValueError("Input file has wrong column names: {}".format(5))
        for row in it:
            if len(row) == 1:
                row += (None,)
            yield SentimentTrainer(*row)   
            
    def make_train_test_split(self,seed, proportion=0.9):

        data = list(pred._iter_data_file('sentiment_graded.csv'))
        
        ids = list(sorted(set(x.long_comment for x in data)))
        print ids
        N = int(len(ids) * proportion)
        if N == 0:
            N += 1
        rng = random.Random(seed)
        rng.shuffle(ids)
        test_ids = set(ids[N:])
        train = []
        test = []
        for x in data:
            if x.long_comment in test_ids:
                test.append(x)
            else:
                train.append(x)
        
        return train, test    
    
    def make_long_comment_as_data(self,long_comment):
        test_list=[]
        for i in long_comment:
            test_list.append(SentimentTrainer(phrase=i))
        test_list

    
if __name__ == '__main__':
    pred=Parser(); 
    train, test = pred.make_train_test_split("good")
    predictor = Prediction()
    predictor.fit(train)
    predictions= predictor.predict(test)
    print predictions

    