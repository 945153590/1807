height = float(input('请输入身高：'))
money = float(input('请输入身价：'))
yanzhi = int(input('请输入颜值分：'))
if (height >= 180) and (money >= 1000000) and (yanzhi >= 99):
	print('高富帅')
elif (money >= 10000) and (yanzhi >= 99):
	print('富帅')
elif yanzhi >= 99:
	print('帅')
elif (height < 160) and (money < 100) and (yanzhi <60):
	print('矮矬穷')
else:
	print('一般')
