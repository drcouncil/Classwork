import socket
import sys

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

address = ('localhost',5000)
client_socket.connect(address)
text = raw_input( "Type: ")
client_socket.sendall(text)
b=client_socket.recv(1024)

print b
