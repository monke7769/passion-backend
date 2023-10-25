# imports and object oriented programming
import pandas as pd
from rsa import rsa
from caesar import caesar
from substitution import substitution
from binary import binary
import random
from rsa import rsa
# This program will create data for training an ai to classify a cipher, whcih will then be used to decrypt the message

# data formatting and splitting into division for creating dataset for each cipher
df=pd.read_csv('Emotion_final.csv') # reading from a public database I imported in
# print(df['Text'])
divisions=[]
# ciphers ceaser, rsa, vinegar, binary, hexadecimal
# print(len(df['Text']))
ciphers={'ceaser':[],'rsa':[],'binary':[],'hexadecimal':[],'substitution':[]} # dictionary that will contain all of the text
names=['ceaser','rsa','substitution','hexadecimal','binary'] # name of each cipher
index=-1

# going through all text and assigning to a cipher
for i in range(len(df['Text'])):
    ciphers[names[index]].append(df['Text'][i])
    if(i%4291==0):
        index+=1
    if(index>4):
        break

import csv

new_row = [["Text","Cipher"]]

with open('data.csv', 'a', newline='') as file: # doing a csv write of all of the text,cipher stuff
    
    writer = csv.writer(file)
    writer.writerows(new_row)
    
    # looping through each cipher text and adding encoded text/cipher name for trainig classification of the cipher
    for i in range(ciphers['ceaser']):
        writer = csv.writer(file)
        val=random.randint(1,26)
        cea=caesar(val,ciphers['ceaser'][i])
        new_row=[[cea.encrypt(),'ceaser']]
        writer.writerows(new_row)
        
    for i in range(ciphers['rsa']):
        writer = csv.writer(file)
        rsaobject=rsa()
        new_row=[[ciphers['rsa'][i],'rsa']]
        writer.writerows(new_row)
        
    for i in range(ciphers['binary']):
        bin=binary(ciphers['binary'][i])
        writer = csv.writer(file)
        new_row=[[bin.encrypt(),'binary']]
        writer.writerows(new_row)
        
    for i in range(ciphers['substitution']):
        val=random.randint(1,26)
        sub=substitution(val,ciphers['substitution'][i] )
        writer = csv.writer(file)
        new_row=[[sub.encrypt(),'substitution']]
        writer.writerows(new_row)
        
    for i in range(ciphers['hexadecimal']):
        
        writer = csv.writer(file)
        new_row=[[ciphers['hexadecimal'][i],'hexadecimal']]
        writer.writerows(new_row)