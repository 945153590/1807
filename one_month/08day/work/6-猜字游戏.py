i = 0
import random
c = random.randint(1,100)
while i < 10:
	a = int(input('请输入一个数字：'))
	if a > c:
		print('猜大了')
	elif a < c:
		print('猜小了')
	else:
		print('猜对了')
		break
	i+=1
