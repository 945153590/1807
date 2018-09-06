from socket import *

# 创建一个udp的套嵌套字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('', 5000))

# 对方ip 端口
s.sendto('我是老王'.encode('gb2312'), ('192.168.56.1', 8080))


while True:
	ret = s.recvfrom(1024)
	print(ret)
	print(ret[0].decode('gb2312'))	
	print(ret[1][0])
	print(ret[1][1])
s.close()
