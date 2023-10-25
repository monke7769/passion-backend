# By: Shuban Pal
# Algorithm: Morse Code
# Project: CSP Passion Project
# Date: 2023
class morse:
  def __init__(self, text):
    self.text = text
  def encrypt(enc):
    dex = {
      "A": ".-",
      "B": "-...",
      "C": "-.-.",
      "D": "-..",
      "E": ".",
      "F": "..-.",
      "G": "--.",
      "H": "....",
      "I": "..",
      "J": ".---",
      "K": "-.-",
      "L": ".-..",
      "M": "--",
      "N": "-.",
      "O": "---",
      "P": ".--.",
      "Q": "--.-",
      "R": ".-.",
      "S": "...",
      "T": "-",
      "U": "..-",
      "V": "...-",
      "W": ".--",
      "X": "-..-",
      "Y": "-.--",
      "Z": "--..",
      " ": "/",
    }
    ptparse = []
    ct = ""
    for i in range(0,len(enc.text)):
      ptparse.append(enc.text[i].upper())
    for j in range(0,len(ptparse)):
      ct += dex[ptparse[j]]
      ct += " "
    return ct
      

  def decrypt(dec):
    inverted_dex = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '/': ' ',
    }
    ctparse = dec.text.split(" ")
    pt = ""
    for i in range(0,len(ctparse)):
      pt += inverted_dex[ctparse[i]]
    return pt
    

mycipher = morse("Hello World") 
print(mycipher.encrypt())
cipher2 = morse(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
print(cipher2.decrypt())
