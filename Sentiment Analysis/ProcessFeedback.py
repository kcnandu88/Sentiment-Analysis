'''
Created on Jul 18, 2015

@author: Nandu
'''


import datetime 
import pandas
import numpy as np
 

class FeedbackProcessor():
    
    def get_unix(self, deliveryunixdate):    
        lis = []
        for i in deliveryunixdate:
            ts = (i - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
            if (pandas.isnull(ts) != True):
                if ts != -62135593200.0:
                    if  ts != -62075113200.0:
                        if ts != 91464944400.0:
                            lis.append(datetime.datetime.utcfromtimestamp(ts))
                        else:
                            lis.append(-9223372036854)    
                    else:
                        lis.append(-9223372036854)   
                else:
                            lis.append(-9223372036854)
            else:
                            lis.append(-9223372036854)    
        
        return np.array(lis) 
        
    def __init__(self):
        
        self.load()
    
    def get_unixtime(self, deliveryunixdate):    
        
        return (deliveryunixdate.astype(np.int64) / 1e6).astype(np.int64)    
    
    def load(self):
        data12 = pandas.read_csv(open("feedback.csv"), sep=",", usecols=[0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 15, 16, 18, 19, 20, 21])
        
        data1 = np.array(data12)
        
        a = pandas.to_datetime(data1[:, 9], utc=True)
        a1 = pandas.to_datetime(data1[:, 11], utc=True)
        a3 = pandas.to_datetime(data1[:, 10], utc=True)
        df = a1.tolist()
        da = []
        for i in df:
            if pandas.isnull(i) != True:
                b_s = bytearray(i)
                b_s[12] = "1"    
                da.append(b_s.decode("utf-8"))
            else:
                da.append("")
        a2 = pandas.to_datetime(da)
        
        b = np.array(a, dtype=np.datetime64)
        
        b1 = np.array(a2, dtype=np.datetime64)
        
        b2 = np.array(a3, dtype=np.datetime64)
        
        self.deliveryTime = self.get_unixtime(b)
        self.eta = self.get_unix(b1)
        self.short_comment = data1[:, 0]
        self.long_comment = data1[:, 3]
        self.ship_date = self.get_unixtime(b2)
        self.overall_score = data1[:, 12]
        self.item_condition = data1[:, 14]
        self.packaging_score = data1[:, 13]
        self.uidesign = data1[:, 15]        
        
data = FeedbackProcessor();
 