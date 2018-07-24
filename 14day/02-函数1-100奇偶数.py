def num():
	for i in range(1,101):
		if i%2 == 0:
			print('我是偶数:%d'%i,end = '    ')
			print('')
		else:
			print('我是奇数:%d'%i,end= '        ')
num()
