a = '123456'
p = 'abc'
c = input('请输入账号：')
d = input('请输入密码：')
if a == c and p == d:
	print('登录成功')
elif a == c and p != d:
	print('密码错误')
elif a != c and p == d:
	print('账号错误')
else:
	print('账号和密码错误')
