from socket import *
from threading import *
import time

# 创建一个udp的套嵌套字
s = socket(AF_INET,SOCK_DGRAM)
#s.bind(('', 5000))

def puton(i):

	# 对方ip 端口
	s.sendto(i.encode('gb2312'), ('192.168.56.1', 8080))
	time.sleep(1)

def putout():
	while True:
		ret = s.recvfrom(1024)
		print(ret)
		print(ret[0].decode('gb2312'))	
		print(ret[1][0])
		print(ret[1][1])

if __name__ == '__main__':
	while True:
		i = input('输入信息：')
		if len(i) != 0:
			t = Thread(target=puton, args=(i,))
			t.start()
			t.join()
			t1 = Thread(target=putout)
			t1.start

s.close()
