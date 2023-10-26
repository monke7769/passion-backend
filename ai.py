# imports
from sklearn.feature_extraction.text import CountVectorizer # converting text to numbers
from sklearn.naive_bayes import MultinomialNB #Naive Bayes Multinomial Algorthim AI model
from sklearn.model_selection import train_test_split # Data Formatting
from sklearn.metrics import accuracy_score, classification_report # scoring the model
import pandas as pd
import numpy as np
from sklearn.svm import SVC
class ai:
    def __init__(self,filename):
        self.data=pd.read_csv(filename) # reading input in
        self.ciphers=['Cipher','ceaser','morse','substitution','hexadecimal','binary'] # cipher name list
        self.vectorizer = CountVectorizer() # creating the bag-of-words
        
        
    def preprocess(self): # preprocessing or training
        self.vectorizer.fit(self.data['Text'])
        self.X = self.vectorizer.transform(self.data['Text']) # transofrming the input text for training
        Y_series=self.data['Cipher']
        Y_encoded=[]
        for i in Y_series:
            if(i!='Cipher'):
                Y_encoded.append(self.ciphers.index(i)) # categorical encoding matching number to output text
        self.Y=pd.Series(Y_encoded)
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.Y, test_size=0.2, random_state=42)
        
    def evalulate(self):
        clf = SVC(kernel='linear') # creating Support Vector Machine Model
        clf.fit(self.X_train, self.Y_train) # Training
        Y_train_pred=clf.predict(self.X_train) # predicting for training accuracy
        Y_pred = clf.predict(self.X_test) # predicting the testing model data

        # Accuracy for testing and training to check overfit and underfit
        train_accuracy=accuracy_score(self.Y_train,Y_train_pred)
        test_accuracy = accuracy_score(self.Y_test, Y_pred)
        print('Test accuracy',test_accuracy,'Train Accuracy', train_accuracy) # printing it out
        
        
        
        
        
    


