x = float(input('请输入x值：'))
z = input('请输入+-*/:')
y = float(input('请输入y值：'))
if z == '+':
	print(x+y)
elif z == '-':
	print(x-y)
elif z == '*':
	print(x*y)
elif z == '/':
	if y == 0:
		print('不合法')
	else:
		print(x/y)
else:
	print('error')
