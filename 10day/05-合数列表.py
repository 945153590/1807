'''
num = []
for i in range(2,101):
	for j in range(2,i):
		if i%j == 0:
			num.append(i)
			break
print(num)
'''
num = []
i = 2
while i < 101:
	j = 2
	while j < i:
		if i%j == 0:
			num.append(i)
			break
		j+=1
	i+=1
print(num)
