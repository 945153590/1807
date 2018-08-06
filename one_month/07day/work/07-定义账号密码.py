a = 123456
p = 'abc'
c = int(input('请输入账号：'))
d = input('请输入密码：')
if a == c and p == d:
	print('登录成功')
elif (a != c and p == d) or (a == c and p != d):
	print('账号或密码错误')
