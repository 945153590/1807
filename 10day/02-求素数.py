'''
素数只能被1和本身整除
任何数字都能被1和本身整除
任何数字都不能被比它大的数整除
'''
'''
for i in range(2,101):
	flag = 1#立下的假设
	for j in range(2,i):
		if i%j == 0:#当i能被j整除时
			flag = 0#改变我的假设
			break
	if flag == 1:
		print(i)
'''
import random
a = random.randint(2,100)
b = int(input('请输入一个整数：'))
flag = 1
for i in range(2,a):
	if a%i==0:
		flag == 0
	elif flag == 1:
		print('素数')
		break











