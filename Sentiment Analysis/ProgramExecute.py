'''
Created on Jul 23, 2015

@author: Nandu
'''
from File_parsing import Parser
from Predictor import Prediction
from Analysis import Analysis
from ProcessFeedback import FeedbackProcessor
from Data import SentimentTrainer
from Pearson_Correlation import Pearson


if __name__ == '__main__':
    feedback=FeedbackProcessor()