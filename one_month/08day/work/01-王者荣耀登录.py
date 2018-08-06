ac = 'wangzherongyao'
pa = 123456
i = 0
while i < 3:
	a = input('账号：')
	p = int(input('密码：'))
	if a == ac and p == pa:
		print('登录成功')
		hero = int(input('请选择英雄1:ADC 2:肉 3：法师:'))
		if hero == 1:
			print('鲁班')
		elif hero == 2:
			print('程咬金')
		elif hero == 3:
			print('王昭君')
		break
	else:
		print('请重新输入')
	i+=1
'''
hero = input('请选择英雄1:ADC 2:肉 3：法师:')
if hero == 1:
	print('鲁班')
if hero == 2:
	print('王昭君')
if hero == 3:
	print('程咬金')
'''
