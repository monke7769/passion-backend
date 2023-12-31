import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
from aienglishprediction import aienglishprediction
from flask_cors import CORS
# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from rsa import RSA # import RSA cipher

from flask import Flask, render_template, request, jsonify
from urllib.parse import quote as url_quote
import subprocess
import os
from caesar import caesar as c1 # first cipher ceasar
from substitution import substitution as c2 # second cipher subtitution
from generate import generate as gn # importing the generator api
from morse import morse # importing morse cipher
from binary import binary # importing binary cipher
from hex import hexadecimal # importing hexadecimal cipher
from aiprediction import aiprediction # importing the ai prediciton class
app = Flask(__name__)
CORS(app)


# Initialize the SQLAlchemy object to work with the Flask app instance
# db.init_app(app)

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")

@app.route("/caesarencrypt", methods=["POST"])
def caesarencrypt():
    text = request.json.get("text")  # getting the text
    print(text)
    gen=gn()  # creating api random generator class
    value=gen.getrandom(1)[0] # getting random number
    cipher1=c1(int(value),text)
    encrypted = cipher1.encrypt() # encrypting with ceasar cipher
    print(encrypted)
    return jsonify(str(encrypted))

@app.route("/morseencrypt", methods=["POST"])
def morseencrypt():
    text = request.json.get("text")  # getting the text
    morseobject = morse(text) # creating morse object
    encrypted = morseobject.encrypt() # encrypting with morse code
    print(encrypted)
    return jsonify(str(encrypted)) # outputting morse encrypted ode

@app.route("/binaryencrypt", methods=["POST"])
def binaryencrypt():
    text = request.json.get("text") # getting the text
    bin=binary(text)
    encrypted = bin.encrypt() # encrypting with binary cipher
    print(encrypted)
    return jsonify(str(encrypted)) # returning the encrypted value

@app.route("/hexencrypt", methods=["POST"])
def hexencrypt():
    text = request.json.get("text") # getting textbox words
    hex=hexadecimal(text) # creating hexadecimal object
    encrypted=hex.encrypt() # encryptihg with hexadecimal cipher
    print(encrypted)
    return jsonify(str(encrypted)) # outputting string

@app.route("/subencrypt", methods=["POST"])
def subencrypt():
    text = request.json.get("text") # getting the text
    gen=gn()
    value=gen.getrandom(1)[0] # getting random number from api
    sub=subencrypt(value,text)
    encrypted = sub.encrypt() # substitution cipher
    print(encrypted)
    return jsonify(str(encrypted))

@app.route("/rsaencrypt", methods=["POST"])
def rsa():
    text = request.json.get("text") # getting text
    print('here')
    rsaobj=RSA()
    rsa = RSA(bits=2048) # initializing the RSA object
    print("Created Object")
    plaintext = text
    plaintext = int.from_bytes(plaintext.encode(), byteorder='big') # setup code

    ciphertext = rsa.rsa_encrypt(plaintext) # encrypting with rsa
    
    print(ciphertext)
    
    return jsonify(str(ciphertext))

@app.route("/decrypt", methods=["POST"])
def decrypt():
    text = request.json.get("text") # getting text
    output=""
    predictor=aiprediction()
    value=predictor.pred(text)
    eng=aienglishprediction()
    if(value=="binary"): # checking for binary cipher
        object=binary(text)
        output=object.decrypt()
    elif(value=="hexadecimal"): # checking for hexadecimal cipher
        object=hexadecimal(text)
        output= object.decrypt()
    elif(value=="morse"): # checking for morse cipher
        object=morse(text)
        output= object.decrypt()
    else:  
        for key in range(1,27): # going through all possibly keys(brute forcing)
            eng=aienglishprediction() # creating an object of the ai class
            objecter=c1(key,text) 
            print(value)
            if value == "ceasar": # checking which cipher
                objecter = c1(key, text) # creating object for ceasar
            elif value == "substitution":
                objecter = c2(key, text) # creating object for substitution
            if eng.predict(objecter.decrypt()) == 0: # decrypting and seeing if it's close to english
                output= objecter.decrypt()
    return jsonify(str(output)) # returning the output


if __name__ == "__main__":
    
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8080")
