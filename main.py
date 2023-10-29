import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

from flask_cors import CORS
# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from rsa import RSA

from flask import Flask, render_template, request, jsonify
from urllib.parse import quote as url_quote
import subprocess
import os
from caesar import caesar as c1 # first cipher
from substitution import substitution as c2 # second cipher
from generate import generate as gn
from morse import morse
from binary import binary
from hex import hexadecimal
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
    text = request.json.get("text")
    print(text)
    gen=gn()
    value=gen.getrandom(1)[0]
    cipher1=c1(int(value),text)
    encrypted = cipher1.encrypt()
    print(encrypted)
    return jsonify(str(encrypted))

@app.route("/morseencrypt", methods=["POST"])
def morseencrypt():
    text = request.json.get("text")
    morseobject = morse(text)
    encrypted = morseobject.encrypt()
    print(encrypted)
    return jsonify(str(encrypted))

@app.route("/binaryencrypt", methods=["POST"])
def binaryencrypt():
    text = request.json.get("text")
    bin=binary(text)
    encrypted = bin.encrypt()
    print(encrypted)
    return jsonify(str(encrypted))

@app.route("/hexencrypt", methods=["POST"])
def hexencrypt():
    text = request.json.get("text")
    hex=hexadecimal(text)
    encrypted=hex.encrypt()
    print(encrypted)
    return jsonify(str(encrypted))

@app.route("/subencrypt", methods=["POST"])
def subencrypt():
    text = request.json.get("text")
    gen=gn()
    value=gen.getrandom(1)[0]
    sub=subencrypt(value,text)
    encrypted = sub.encrypt()
    print(encrypted)
    return jsonify(str(encrypted))

def rsa():
    text = request.json.get("text")
    rsaobj=RSA()
    rsa = RSA(bits=2048)
    plaintext = text
    plaintext = int.from_bytes(plaintext.encode(), byteorder='big')

    ciphertext = rsa.rsa_encrypt(plaintext)
    
    print(ciphertext)
    
    return jsonify(str(ciphertext))


if __name__ == "__main__":
    
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8080")