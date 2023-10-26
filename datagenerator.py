# imports and object oriented programming
import pandas as pd
from rsa import RSA
from caesar import caesar
from substitution import substitution
from binary import binary
import random
from hex import hexadecimal
from morse import morse
# This program will create data for training an ai to classify a cipher, whcih will then be used to decrypt the message

# data formatting and splitting into division for creating dataset for each cipher
df=pd.read_csv('Emotion_final.csv') # reading from a public database I imported in
# print(df['Text'])
divisions=[]
# ciphers ceaser, rsa, vinegar, binary, hexadecimal
# print(len(df['Text']))
ciphers={'ceaser':[],'morse':[],'binary':[],'hexadecimal':[],'substitution':[]} # dictionary that will contain all of the text
names=['ceaser','morse','substitution','hexadecimal','binary'] # name of each cipher
index=-1

# going through all text and assigning to a cipher
for i in range(len(df['Text'])):
    ciphers[names[index]].append(df['Text'][i])
    if(i%4291==0):
        index+=1
    if(index>4):
        break
print(len(ciphers['morse']))

import csv
print(len(ciphers['ceaser']))
new_row = [["Text","Cipher"]]

with open('data.csv', 'a', newline='') as file: # doing a csv write of all of the text,cipher stuff
    
    writer = csv.writer(file)
    writer.writerows(new_row)
    
    # looping through each cipher text and adding encoded text/cipher name for trainig classification of the cipher
    print("thing")
    for i in range(len(ciphers['ceaser'])):
        
        val=random.randint(1,26)
        cea=caesar(val,ciphers['ceaser'][i])
        new_row=[[cea.encrypt(),'ceaser']]
        # print(new_row,ciphers['ceaser'][i])
        writer.writerows(new_row) 
    
    for i in range(len(ciphers['morse'])):
        morseobject = morse(ciphers['morse'][i])
        new_row=[[morseobject.encrypt(),'morse']]
        writer.writerows(new_row)
        
    for i in range(len(ciphers['binary'])):
        bin=binary(ciphers['binary'][i])
        new_row=[[bin.encrypt(),'binary']]
        writer.writerows(new_row)
        
    for i in range(len(ciphers['substitution'])):
        val=random.randint(1,26)
        sub=substitution(val,ciphers['substitution'][i] )
        
        new_row=[[sub.encrypt(),'substitution']]
        writer.writerows(new_row)
        
    for i in range(len(ciphers['hexadecimal'])):
        hexa= hexadecimal(ciphers['hexadecimal'][i])
        
        new_row=[[hexa.encrypt(),'hexadecimal']]
        writer.writerows(new_row)
    
    
    