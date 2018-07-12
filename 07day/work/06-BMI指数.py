H = float(input('请输入身高以米为单位：'))
W = float(input('请输入体重以kg为单位：'))
bmi = W / H**2
if bmi < 18.5:
	print('过轻')
elif bmi >= 18.5 and bmi < 25:
	print('正常')
elif bmi >= 25 and bmi < 28:
	print('过重')
elif bmi >= 28 and bmi < 32:
	print('肥胖')
elif bmi > 32:
	print('严重肥胖')
else:
	print('无可救药')
