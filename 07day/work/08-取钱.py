acc = 945153590
pas = 13579
money = 99999999999999999999999
a = int(input('请输入账号：'))
b = int(input('请输入密码：'))
if acc == a and pas == b:
	print('请输入金额')
	c = float(input('金额：'))
	if money < 100:
		print('没钱取毛线')
	elif money > 100 and money-c >= 0:
		print('取了%.02f'%(c),'还剩%.02f'%(money-c))
	else:
		print('账户余额不足')
else:
	print('账号或密码错误')
