
from aienglishprediction import aienglishprediction

from rsa import RSA

from caesar import caesar as c1 # first cipher
from substitution import substitution as c2 # second cipher
from generate import generate as gn
from morse import morse
from binary import binary
from hex import hexadecimal
from aiprediction import aiprediction
def decrypt(text):
    output=""
    predictor=aiprediction()
    value=predictor.pred(text)
    eng=aienglishprediction()
    if(value=="binary"):
        object=binary(text)
        output=object.decrypt()
    elif(value=="hexadecimal"):
        object=hexadecimal(text)
        output= object.decrypt()
    elif(value=="morse"):
        object=morse(text)
        output= object.decrypt()
    else:  
        for key in range(1,27):
            eng=aienglishprediction()
            objecter=c1(key,text)
            print(value)
            if value == "ceasar":
                objecter = c1(key, text)
            elif value == "substitution":
                objecter = c2(key, text)
            if eng.predict(objecter.decrypt()) == 0:
                output= objecter.decrypt()
    return output

thing=decrypt('L uhdooob oryh wr frgh vlqfh lw lqyroyhv vr pdqb frro wklqjv')
print(thing)