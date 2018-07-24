list = []

def showError(msg):
	print('输入有误,请重新输入'+msg)

def add():#添加学生
	d = {}
	while True:
		name = input('请输入姓名：')
		if len(name) >= 2 and len(name) <= 4:
			d['name'] = name
			break
		else:
			showError('，姓名必须在2~4个字符之间')
	while True:
		age = input('请输入年龄：')
		if age.isdigit():
			age = int(age)
		else:
			showError(',年龄必须为数字')
			continue
		if age >=1 and age <= 130:
			d['age'] = age
			break
		else:
			showError('，年龄必须在1~130岁之间')
	while True:
		sex = input('请输入性别：')
		if sex == '男' or sex == '女':
			d['sex'] = sex
			break
		else:
			showError('性别必须为男或女')
	list.append(d)
	print('添加成功')
def find():#查找学生
	print('-'*50)
	name = input('请输入姓名：')
	for d in list:
		if d['name'] == name:
			print('学生姓名：%s\n学生年龄：%d\n学生性别：%s'%(d['name'],d['age'],d['sex']))
			break
		else:
			pass
def change():#修改信息
	print('-'*50)
	name = input('请输入姓名：')
	for d in list:
		if d['name'] == name:
			print('学生姓名：%s\n学生年龄：%d\n学生性别：%s'%(d['name'],d['age'],d['sex']))
			print('-'*50)
			print('1：修改学生姓名')
			print('2：修改学生年龄')
			print('3：修改学生性别')
			num = int(input('请选择功能：'))
			if num == 1:
				name = input('请输入新姓名：')
				d['name'] = name
			elif num == 2:
				age = int(input('请输入新年龄：'))
				d['age'] = age
			elif num == 3:
				sex = input('请输入性别：')
				d['sex'] = sex
			print('修改成功')
			break
		else:
			pass

def delete():#删除学生
	print('-'*50)
	name = input('请输入学生姓名：')
	for d in list:
		if d['name'] == name:
			list.remove(d)
			print('删除成功')
			break
		else:
			pass

def print_list():#打印信息
	print('姓名          年龄          性别          ')
	for d in list:
		print(d['name'],end = '           ')
		print(d['age'],end = '            ')
		print(d['sex'],end = '            ')
		print('')
def print_menu():#显示功能
	print('*'*50)
	print('欢迎来到学生管理系统'.center(40,' '))
	while True:
		print('0:退出系统')
		print('1:添加学生信息')
		print('2:查找学生信息')
		print('3:修改学生信息')
		print('4:删除学生信息')
		print('5:打印学生信息')
		input_info()#调用选择功能函数

def input_info():#选择功能
	print('-'*50)
	num = int(input('请选择功能：'))
	if num == 1:
		add()
	elif num == 2:
		find()
	elif num == 3:
		change()
	elif num == 4:
		delete()
	elif num == 5:
		print_list()
	elif num == 0:
		exit()

print_menu()
print('*'*50)









