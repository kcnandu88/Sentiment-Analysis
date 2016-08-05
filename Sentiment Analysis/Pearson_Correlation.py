'''
Created on Jul 20, 2015

@author: Nandu
'''
from __future__ import division
import ProcessFeedback as pro
import numpy as np


class Pearson(object):
    '''
    classdocs
    '''
    def calculate_weightage(self, overall_score, item_condition, packaging_score):
        positive = []  
        negative = []      
        self.posneg = []
        for i in range(len(overall_score)):
            weight = 0;
            if np.isnan(overall_score[i]) != True:
                weight += overall_score[i] * .5
            if np.isnan(item_condition[i]) != True:
                weight += item_condition[i] * .25
            if np.isnan(packaging_score[i]) != True:
                weight += packaging_score[i] * .25
            self.posneg.append(weight)
#             if(weight > 3.99):
#                 positive.append(weight)
#             else:
#                 negative.append(weight)
        # print len(positive),len(negative)
        return self.posneg

    def calculate_pearson(self, x, y):
        print np.corrcoef(x, y)
     
    def linear_regression(self, x, y):
        regression = np.polyfit(x, y, 1)
        return regression
    
