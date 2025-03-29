from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
cypher_num = input("Choose the type of cypher:\n(1)reverse\n(2)caesar\n(3)random\n")
message = ''
match cypher_num:
    case '1':
        message += "reverse "
    case '2':
        message += "caesar "
    case '3':
        message += "random "

plain_text = input("Type the text to be encrypted:\n")
message += r'"' + plain_text + r'"'

s.send(str.encode(message))  # send some data
data = s.recv(1024)     # receive the response
print (bytes.decode(data))            # print the result
s.close()               # close the connection
