x = float(input('请输入x值：'))
z = input('请选择+-*/**：')
y = float(input('请输入y值：'))
if z == '+':
	print(x+y)
elif z == '-':
	print(x-y)
elif z == '*':
	print(x*y)
elif z == '/':
	if y == 0:
		print('0不能做除数')
	else:
		print(x/y)
elif z == '**':
	print(x**y)
else:
	print('error')
