list = [34,2,14,44,23,1,98,70,55]
for i in range(0,len(list)-1):
	for j in range(i+1,len(list)):
		if list[i] > list[j]:
			list[i],list[j] = list[j],list[i]
	print(list)

