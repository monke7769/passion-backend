import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

class aienglish:
    def __init__(self):
        # Load the dataset
       self. df = pd.read_csv('datatrainisenglish.csv')
    
    def preprocess(self):

    # Split the data
        self.X = self.df['Text']
        self.y = self.df['IsEnc']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # TF-IDF vectorization
        self.tfidf_vectorizer = TfidfVectorizer()
        self.X_train_tfidf = self.tfidf_vectorizer.fit_transform(self.X_train)
        self.X_test_tfidf = self.tfidf_vectorizer.transform(self.X_test)
    def train(self):
    # Train a Logistic Regression model
        self.model = LogisticRegression()
        self.model.fit(self.X_train_tfidf, self.y_train)

        # Make predictions
        y_pred =self.model.predict(self.X_test_tfidf)

        # Evaluate the model
        accuracy = accuracy_score(self.y_test, y_pred)
        report = classification_report(self.y_test, y_pred)
        print("Accuracy:", accuracy)
    def export(self):
        

        joblib.dump(self.model, "Checkingenglishmodel.joblib")

        # Save the vectorizer to a file
        joblib.dump(self.tfidf_vectorizer, "vectorizerenglish.joblib")

