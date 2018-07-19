list = []#空列表
for i in range(3):
	d = {}#空字典
	name = input('请输入姓名：')
	age = input('请输入年龄：')
	sex = input('请输入性别：')
	d['name'] = name#将键和值添加到字典中
	d['age'] = age
	d['sex'] = sex
	print(d)#打印字典
	list.append(d)#将字典添加列表中
print(list)
for i in list:#遍历出字典
	for j,k in i.items():#遍历出值
		print(j,k)
