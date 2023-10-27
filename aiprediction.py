from keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from keras.models import model_from_json
import joblib
from caesar import caesar
class aiprediction:
    def __init__(self):
        self.ciphers=['Cipher','ceaser','morse','substitution','hexadecimal','binary'] # cipher name list

        vectorizer = CountVectorizer()
        with open("model.json", "r") as json_file:
            loaded_model_json = json_file.read()

        self.loaded_model = model_from_json(loaded_model_json)

        # Load the model weights from the HDF5 file
        self.loaded_model.load_weights("model1.h5")

        self.loaded_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    def pred(self,text):
        #A BUNCH OF EXAMPLES
        
        #binary example
        #example = "10001100000000021110010000000002110111100000000211011010000000021000000000000021100001000000002100000000000002111001100000000211101000000000021100001000000002111001000000000211101100000000021101001000000002110111000000000211001110000000021000000000000021110011000000002111010000000000211100100000000021100001000000002111100100000000210000000000000211010010000000021110100000000002100000000000002111011100000000211000010000000021110011000000002100000000000002111010000000000211100100000000021100001000000002110111000000000211100110000000021100110000000002110111100000000211100100000000021101101000000002110010100000000211001000000000021000000000000021101001000000002110111000000000211101000000000021101111000000002100000000000002110000100000000210000000000000211000110000000021101111000000002110111000000000211101000000000021100101000000002110111000000000211101000000000021100101000000002110010000000000210000000000000211010000000000021101111000000002111010100000000211100110000000021100101000000002100000000000002"

        #Caesar Example
        #cae=caesar(7," I love to do some many things including code code code oh how it is so fun yay")
        #example=cae.encrypt()
        
        
        vectorizer = joblib.load("vectorizer.pkl") # importing back in the input data transformation
        X_new = vectorizer.transform([text]).toarray()
        Ypred = self.loaded_model.predict(X_new)
        Ypfinal = np.argmax(Ypred, axis=1) # predicting it and taking the highest possibility of each output
        
        print("The cipher is", self.ciphers[int(Ypfinal[0])],"cipher")
        return self.ciphers[int(Ypfinal[0])]