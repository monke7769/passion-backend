# By: Shuban Pal
# Algorithm: Caesar
# Project: CSP Passion Project
# Date: 2023

class caesar:
  global key
  def __init__(self, key, text):
    self.key = key
    self.text = text
  def encrypt(enc): # Main encryption algorithm
    ct=""
    for i in range(0,len(enc.text)):
      char = enc.text[i]
      if char.isalpha(): # If character is a part of the alphabet...
        shift = 97 if char.islower() else 65 # Shift by 97 (lowercase a). Else by 65 (uppercase A)
        ct+=chr((ord(char) - shift + enc.key)%26 + shift) # Main caesar encryption with unicode
      else:
        ct += char # Append the encrypted char into ciphertext
    return ct
  
  def decrypt(dec, keyval):  # Main decryption algorithm
    pt = ""
    print(keyval, "------")  # Print the current key value
    for i in range(0, len(dec.text)):
        char = dec.text[i]
        if(char==' '):
          pt+=' '
          continue
        shift = 97 if char.islower() else 65  # Same shift as encryption to corresponding case unicode
        pt += chr((ord(char) - shift - keyval) % 26 + shift)  # Subtract from the key to reverse to the original state
    return pt

  
      

mycipher = caesar(3,"Hello World") # Test case: Encrypt string "Hello World" with key of 3
print(mycipher.encrypt())

