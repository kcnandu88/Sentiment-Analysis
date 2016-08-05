'''
Created on Jul 18, 2015

@author: Nandu
'''
from __future__ import division
import datetime 
import pickle
from matplotlib import pyplot as plt
import pandas
from scipy.stats import itemfreq
import ProcessFeedback as pro
import numpy as np
import scipy as sp
import time as dd
import Pearson_Correlation as pearson 


class Analysis(object):
    '''
    classdocs
    '''
    
    '''
    The constructor loads the naive Bayes classifier 
    when initialized. Pickle is used to load and save the model
    '''
    def __init__(self):
        f = open('my_classifier.pickle')
        self.classifier = pickle.load(f)
    
    '''
    returns a dictionary
    
    '''         
    def make_dict(self, comment):
            test = {}
            for i in comment:
                test[i] = True
            return test  
    
    
    '''
    The function calculates the sentiment of the long_comment depending on the delivery dates
    returns a dictionary of time of delivery where negative comments are given
    '''
    def negative_time(self, delivered, comment):    
            difference_date = []
            d = {}
            coefficients = []
            # delivered=feedback_sentiment.get_unixtime(delivered_timestamp)
            for i in range(len(delivered)):
                 if (delivered[i] != -9223372036854 and isinstance(comment[i], str) == True):
                    dict = analysis.make_dict(comment[i])
                    value = analysis.classifier.classify(dict)
                    if(value == 'neg'): 
                        coefficients.append(0)
                        tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = dd.gmtime(delivered[i] / 1000)
                        if d.has_key(tm_hour):
                            d[tm_hour] += 1
                        else:
                            d[tm_hour] = 1        
                        # d1=datetime.timedelta(hours=tm_hour, minutes=tm_min )               
                        # difference_date.append(str(d1))
                    elif(value == 'pos'):
                        coefficients.append(5)
                 else:
                    coefficients.append(-1)
            return coefficients, d
    
     
    '''
     Count the frequency of the short comment so that the frequency and the 
     error percentage can be calculated
    '''       
    def short_comment_count(self, values):
        y = itemfreq(values) 
        d = {}
                    
        freq = y[:, 1]
        word = y[:, 0]
        for i in range(len(word)):
            d[word[i]] = freq[i] 
        return d     
    
    '''
    calculate the date difference between the delivered date and the estimated date.
    This gives an idea whether the package is delivered on time or not
    '''
    def date_delay(self, delivered, eta):    
        difference_date = []
        d = {}
        j = 0
        for i in range(len(delivered)):
            if (delivered[i] != -9223372036854 and eta[i] != -9223372036854):
                tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = dd.gmtime(delivered[i] / 1000)
                d1 = datetime.datetime(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec)                                  
                # difference_date.append((d1 - eta[i]).days)
                if d.has_key((d1 - eta[i]).days):
                    d[(d1 - eta[i]).days] += 1
                else:
                    d[(d1 - eta[i]).days] = 1            
        return d
    
    '''
    Plot the Bar graph
    
    '''
    
    def plotting_bar(self, value,title):
        plt.bar(range(len(value)), value.values(), align='center')
        plt.xticks(range(len(value)), value.keys())
        plt.title(title)
        plt.show()

    '''
    Plot the scatter graph
    
    '''        
    def plotting_scatter(self, value,title):
        plt.scatter(range(len(value)), value.values())
        plt.xticks(range(len(value)), value.keys())
        plt.legend(value.keys())
        plt.title(title)
        plt.show()

    '''
    Calculating the error percentage of the short_Comment 
    delivered, not yet delivered, on time, late
    no information
    ''' 
    def calculate_percentage(self, value, total):
        d = {}             
        for i in value.keys():             
            y = ((value.get(i) / total) * 100)
            d[i] = y
        return d
    
    def error(self, f, x, y):
        return sp.sum((f(x) - y) ** 2)    
    
                
analysis = Analysis()

pearson.correlation_p.calculate_weightage(pro.data.overall_score, pro.data.item_condition, pro.data.packaging_score)

date_delay = analysis.date_delay(pro.data.deliveryTime, pro.data.eta)    
 
negativetime, negative_time_delay = analysis.negative_time(pro.data.deliveryTime, pro.data.long_comment)

pearson.correlation_p.calculate_pearson(np.asarray(negativetime), np.asarray(pearson.correlation_p.posneg))

fp1 = pearson.correlation_p.linear_regression(np.asarray(negativetime), np.asarray(pearson.correlation_p.posneg))


