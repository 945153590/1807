list = [1,3,5,6,7,8,9,10,23]
min = 0#索引最小值
max = len(list)-1#索引最大值
count = 10#要找的数字
while True:
	center = int((min+max)/2)#索引的中间值
	if list[center] > count:
		max = center - 1
	elif list[center] < count:
		min = center + 1
	elif list[center] == count:
		print(list)
		print('索引是%d'%center)
		break
