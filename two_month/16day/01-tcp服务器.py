from socket import *

s = socket(AF_INET, SOCK_STREAM)# 创建tcp
s.bind(('', 7788))

s.listen(5) # 监听

s1, info = s.accept() # 等着接电话
print('有新链接了')

print(s1.recv(1024).decode('gb2313'))
s1.send('haha'.encode('gb2312'))

s.close()
s1.close()
