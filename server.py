from socket  import *
from constCS import * #-

import re
import random

def reverse_encrypt(plain_text):
  encrypted_text = ''
  i = len(plain_text) -1

  while(i >= 0):
    encrypted_text = encrypted_text + plain_text[i]
    i = i - 1
  return encrypted_text

def caesar_encrypt(plain_text):
  encrypted_text = ''

  for i in range(len(plain_text)):
    char = plain_text[i]
    displacement = 4

    if(char.isupper()):
      encrypted_text += chr((ord(char)- 65 + displacement)%26 + 65)
    elif(char.islower()):
      encrypted_text += chr((ord(char)- 97 + displacement)%26 + 97)
    else:
      encrypted_text += char
    
  return encrypted_text

def random_encrypt(plain_text):
  encrypted_text = ""

  for i in range(len(plain_text)):
    char = plain_text[i]

    if(char.isupper()):
      encrypted_text += chr((ord(char)- 65 + random.randint(0,26))%26 + 65)
    elif(char.islower()):
      encrypted_text += chr((ord(char)- 97 + random.randint(0,26))%26 + 97)
    else:
      encrypted_text += char
  
  return encrypted_text

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  message = data.decode()

  match = re.match(r'(\w+)\s+\"([^"]+)\"', message)
  cypher_type = match.group(1)
  plain_text = match.group(2)

  match cypher_type:
    case 'reverse':
      encrypted_text = reverse_encrypt(plain_text)
      conn.send(str.encode(encrypted_text))
    case 'caesar':
      encrypted_text = caesar_encrypt(plain_text)
      conn.send(str.encode(encrypted_text))
    case 'random':
      encrypted_text = random_encrypt(plain_text)
      conn.send(str.encode(encrypted_text))

  
conn.close()               # close the connection
