from flask import Flask, render_template, request, jsonify, url_quote
from urllib.parse import quote as url_quote
import subprocess
import os
from caesar import caesar as c1 # first cipher
from substitution import substitution as c2 # second cipher
from generate import generate as gn

app = Flask(__name__)

@app.route("/")
def index():
    # Construct the absolute path to the Markdown file
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():
    text = request.json.get("text")
    print(text)
    gen=gn()
    value=gen.getrandom(1)[0]
    cipher1=c1(int(value),text)
    encrypted = cipher1.encrypt()
    print(encrypted)
    
    return jsonify("Encrypted Values: "+str(encrypted))

if __name__ == "__main__":
     app.run(debug=True)