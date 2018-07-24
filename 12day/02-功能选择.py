num = input('请选择功能：')
if num.isdigit() and len(num) == 1:
	int(num)
else:
	print('输入错误')
