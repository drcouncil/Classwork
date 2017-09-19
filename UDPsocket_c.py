import socket 
import sys 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = raw_input("Type: ")
sock.sendto(data,('localhost',5421))


data1, addr = sock.recvfrom(2000)
print " message was: " , data1