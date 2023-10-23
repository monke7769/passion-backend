# By: Shuban Pal
# Algorithm: Substitution
# Project: CSP Passion Project
# Date: 2023

class substitution:
  def __init__(self, key, text):
    self.key = key
    self.text = text
  def encrypt(enc):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Alphabet for character positions
    ct=""
    for i in range(0,len(enc.text)):
      if enc.text[i] in alphabet:
        for j in range(0,len(alphabet)): # Replace character with character at the same position but from the key alphabet
          if enc.text[i] == alphabet[j]:
            index = j
        newchar = enc.key[index]
        ct += newchar
      else:
        ct += enc.text[i]
    return ct

  def decrypt(dec):
      alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      pt = ""
      for i in range(0, len(dec.text)):
        if dec.text[i] in alphabet:
          for j in range(0, len(alphabet)):
            if dec.text[i] == dec.key[j]:
              index = j
          newchar = alphabet[index]
          pt += newchar
        else:
          pt += dec.text[i]
      return pt


mycipher = substitution("QWERTYUIOPASDFGHJKLZXCVBNM","ITSSG VGKSR") # Test case: Given a key alphabet and ciphertext, decrypt the ciphertext.
print(mycipher.decrypt())
