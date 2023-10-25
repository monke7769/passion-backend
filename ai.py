# imports
from sklearn.feature_extraction.text import CountVectorizer # converting text to numbers
from sklearn.naive_bayes import MultinomialNB #Naive Bayes Multinomial Algorthim AI model
from sklearn.model_selection import train_test_split # Data Formatting
from sklearn.metrics import accuracy_score, classification_report # scoring the model
import pandas as pd
class ai:
    def __init__(self):
        self.data=pd.read_csv('data.csv')
    


