import random
a = random.randint(1,100)
for i in range(10):
	s = int(input('请输入一个数字:'))
	if s < a:
		print('猜小了，您还有%d次机会'%(10-i-1))
	elif s > a:
		print('猜大了，您还有%d次机会'%(10-i-1))
	else:
		print('猜对了,dashen')
		break
