phone = input('请输入一串数字：')
if phone.startswith('1') and len(phone) == 11:
	print('是手机号')
else:
	print('不是')
