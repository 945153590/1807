z = '后裔'
x = '吕布'
c = '貂蝉'
v = '鲁班'
acc = 123456
pas = 'donglovejin'
print('——'*25)
a = int(input('请输入账号：'))
p = input('请输入密码：')
print('———'*25)
if a == acc and p == pas:
	print('登录成功')
	print('*'*50)
	print('进入游戏')
	print('*'*50)
	hero = input('请选择英雄z：后裔 x：吕布 c：貂蝉 v：鲁班：')
	if hero == 'z' or hero == 'x' or hero == 'c' or hero == 'v':
		print('进入游戏')
	else:
		print('没有此英雄')
else:
	print('账号或密码错误')


