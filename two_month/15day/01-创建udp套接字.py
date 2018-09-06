from socket import *

# 创建一个udp的套嵌套字
s = socket(AF_INET,SOCK_DGRAM)

# 对方ip 端口
s.sendto('我是老王'.encode('gb2312'), ('192.168.56.1', 8080))

s.close()
