i = 1
sum = 0
while i < 10:
	j = 1
	while j <= i:
		sum=j*i
		print('%d×%d=%d'%(j,i,sum),end='\t')
		j+=1
	print('')
	i+=1
