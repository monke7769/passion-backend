# imports
from sklearn.feature_extraction.text import CountVectorizer # converting text to numbers
from sklearn.naive_bayes import MultinomialNB #Naive Bayes Multinomial Algorthim AI model
from sklearn.model_selection import train_test_split # Data Formatting
from sklearn.metrics import accuracy_score, classification_report # scoring the model
import pandas as pd
import numpy as np
from sklearn.svm import SVC # Support Vector Machine
from sklearn.ensemble import RandomForestClassifier # Random Forest
import keras
import joblib
class ai:
    def __init__(self,filename):
        self.data=pd.read_csv(filename) # reading input in
        self.ciphers=['Cipher','ceaser','morse','substitution','hexadecimal','binary'] # cipher name list
        self.vectorizer = CountVectorizer() # creating the bag-of-words
        
        
    def preprocess(self): # preprocessing or training
        self.vectorizer.fit(self.data['Text'])
        self.X = self.vectorizer.transform(self.data['Text']).toarray() # transofrming the input text for training
        Y_series=self.data['Cipher']
        Y_encoded=[]
        for i in Y_series:
            if(i!='Cipher'):
                Y_encoded.append(self.ciphers.index(i)) # categorical encoding matching number to output text
        self.Y=np.array(Y_encoded)
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.Y, test_size=0.3, random_state=42)
        

        
    def train(self):
        model = keras.Sequential([ # creating the model with keras
            keras.layers.Dense(128, activation='relu', input_shape=(self.X.shape[1],)),
            keras.layers.Dropout(0.5),  # Removing percentage nuerons to prevent overfit
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dropout(0.5),  # Removing percentage of nuerons to prevent overfit
            keras.layers.Dense(len(self.ciphers), activation='softmax')
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.model = model
        self.model.fit(self.X_train, self.Y_train, epochs=5, validation_split=0.2)
        # Y_pred =self.model.predict(self.X_test) # predicting the testing model data
        # Y_train_pred=self.model.predict(self.X_train)
        # Accuracy for testing and training to check overfit and underfit
    def export(self):
        model_json = self.model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        # Saving the nueral network weights into the file for quick evaluation and prediction rather than just training+predict every time
        self.model.save_weights("Decryptionclassify.h5")
        print("Checkpoint:THEE Model is Saved") # checkpoint to display that the file is updated
    def evaluate(self):
        print("EVALUATION REPORT","-"*50)
        Y_pred = self.model.predict(self.X_test)  # Predicting the testing model data and the training model data for accuracy later to check stuff
        Y_train_pred = self.model.predict(self.X_train)
        Y_pred_classes = np.argmax(Y_pred, axis=1)
        Y_train_pred_classes = np.argmax(Y_train_pred, axis=1)
        # Getting the score to test how good the model is and to see if overfitting occurs and other issues
        test_accuracy = accuracy_score(self.Y_test, Y_pred_classes)
        train_accuracy = accuracy_score(self.Y_train, Y_train_pred_classes)
        print("Testing Accuracy ", test_accuracy)
        print("Training Accuracy ", train_accuracy)
        
        
        
       
        
        
        
    

