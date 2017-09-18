import socket
import sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(1)
conn,addr=server_socket.accept()
data=conn.recv(1024)
print data
data2 = data.upper()
print data2
conn.sendall(data2)
