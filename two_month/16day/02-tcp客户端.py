from socket import *

s =  socket(AF_INET, SOCK_STREAM)
s.connect(('172.20.10.4', 8080))

s.send('哈哈哈'.encode('gb2312'))

while True:
	msg = s.recv(1024).decode('gb2312')
	print(msg)
