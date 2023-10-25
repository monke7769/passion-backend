# By: Shuban Pal
# Algorithm: Hexadecimal
# Project: CSP Passion Project
# Date: 2023

import binascii

class hexadecimal:
  def __init__(self, text):
    self.text = text
  def encrypt(enc): # Main encryption algorithm
    encbytes = enc.text.encode('utf-8')
    hexverse = binascii.hexlify(encbytes)
    hex_string = hexverse.decode('utf-8')
    return hex_string

  def decrypt(dec): # Main decryption algorithm
    dec.text = dec.text.replace("0x", "")
    bytes_object = bytes.fromhex(dec.text)
    pt = bytes_object.decode("ASCII")
    return pt

mycipher = hexadecimal("Hello World") 
print(mycipher.encrypt())

cipher2 = hexadecimal("48656c6c6f20576f726c64")
print(cipher2.decrypt())
