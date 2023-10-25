# By: Tarun Jaikumar
# Algorithm: Binary 
# Project: CSP Passion Project
# Date: 2023

class binary:
  def __init__(self, text): # inserting text into the class
    self.text = text
  def encrypt(self): # Main encryption algorithm
    encrypted=""
    for character in self.text: # iterating throughe ach character and binary encoding
        encrypted+=bin(ord(character))[2:]+"0"*8+"2" #adding encryption plus 8 zeroes at the end as a seperator since 127 is highest ascii table value and that in binary is 1111111 so no actual character can have 8 zeroes with 2 at the end for distction of character
    return encrypted # return encrypted text
  
  def decrypt(self,encrypted): # binay decryption
    decrypted = ""
    characters = encrypted.split('0' * 8+'2') # splitting by the seperator 
    for char in characters:
        if(char!=''):
            decimal_value = int(char, 2) # base 2 to base 10
            decrypted += chr(decimal_value) # decimal(base 10) back into the character text(ascii table)
    return decrypted # returns decrypted