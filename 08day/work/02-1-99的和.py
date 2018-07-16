'''
sum = 0
sum1 = 0
i = 0
while i < 100:
	if i % 2 == 0:
		sum1=sum1+i
	elif i % 2 == 1:
		sum=sum+i
	i+=1
print('%d-%d=%d'%(sum,sum1,sum-sum1))
'''
sum = 0
i = 1
while i < 100:
	if i % 2 == 1:
		sum+=i
	else:
		sum-=i
	i+=1
print(sum)
