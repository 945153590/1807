a = int(input('请选择一个位置 1：ADC 2：肉盾 3：法师 4：刺客 ：'))
if a < 5 and a > 0:
	if a == 1:
		print('后裔、黄忠、虞姬')
	elif a == 2:
		print('亚瑟、程咬金')
	elif a == 3:
		print('王昭君、妲己')
	elif a == 4:
		print('兰陵王、阿珂')
else:
	print('非法操作')
