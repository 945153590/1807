list = [1,2,3,2,4,5,4,6,7,8,6,5,8,9,3,4,9]
list1 = []
for i in list:
	if i not in list1:
		list1.append(i)
print(list1)
