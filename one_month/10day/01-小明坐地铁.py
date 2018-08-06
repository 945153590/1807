money = 0	#坐地铁所花的钱
d = float(input('请输入距离:'))	#每天的距离
for i in range(1,31):
	print('-'*50)
	print('第%d天坐地铁'%i)
	for j in range(1,3):
		print('第%d次'%j)
		if d <= 6:#6公里以内
			p = 3	#满足公里范围内的单价
		elif d > 6 and d <= 12:
			p = 4
		elif d > 12 and d <= 22:
			p = 5
		elif d > 22 and d <= 32:
			p = 6
		elif d > 32:
			if (d-32)%20 == 0:#超过32公里能被20整除的钱
				p = 6+(d-32)/20
			else:
				p = 6+int((d-32)/20)+1#超过32公里不能被20整除的+1
		#优惠
		if money > 100 and money <= 150:
			p = p*0.8
		elif money > 150 and money <= 400:
			p = p*0.5
		money = money + p#计算总价
print('一共花了%.02f元'%money)



