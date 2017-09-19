import socket 
import sys

UDP_PORT = 5421
UDP= 'localhost'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP,UDP_PORT))
data,addr = server_socket.recvfrom(2000)
print "message:  " , data
data2 = data.upper()
print "upper : " , data2

server_socket.sendto(data2,addr)

