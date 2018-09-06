list = []
d = {}
def add():
	name = input('请输入姓名：')
	sex = input('请输入性别：')
	age = input('请输入年龄：')
	d['name'] = name
	d['sex'] = sex
	d['age'] = age
	list.append(d)
	savecard()
	readcard()
def savecard():
	f = open('card.data','w')
	f.write(str(list))
	f.close()
def readcard():
	f = open('card.data','r')
	content = f.read()
	if len(content) != 0:
		list = eval(content)
	for i in list:
		for k,v in i.items():
			print(k,v)
	print(list)
	f.close()
add()
