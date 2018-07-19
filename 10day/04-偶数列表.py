'''
num = []
for i in range(1,101):
	if i%2 == 0:
		num.append(i)
num.pop(1)
num.remove(20)
print(num)
'''
num = []
i = 1
while i < 101:
	if i%2 == 0:
		num.insert(100,i)
	i+=1
num.pop(1)
num.remove(20)
print(num)
