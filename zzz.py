list = []#空列表存放图书
account = 'library'
password = 'a12345'

def login():#登录界面
	print('*'*50)
	print('欢迎来到图书管理系统'.center(40,' '))#center居中左右空格补冲
	for i in range(3):
		acc = input('请输入账号：'.rjust(21,' '))
		pas = input('请输入密码：'.rjust(21,' '))
		if acc == account and pas == password:
			print('登录成功'.rjust(19,' '))
			showMenu()
			break
		else:
			print('账号或密码错误！'.rjust(23,' '))
			print('您还有%d次机会'%(2-i))

def isNum(num):#判断是否为纯数字
	if num.isdigit():
		return True
	else:
		return False

def showMenu():#功能菜单
	print('-'*50)
	print('0:退 出   系 统'.center(44,' '))
	print('1:增加/归还图书'.center(42,' '))
	print('2:修 改   图 书'.center(44,' '))
	print('3:查 找   图 书'.center(44,' '))
	print('4:借阅/删除图书'.center(42,' '))
	print('-'*50)
	input_info()

def input_info():#功能选择
	while True:
		num = input('请选择功能：')
		if isNum(num):
			num = int(num)
		else:
			print('非法操作')
		if num == 1:
			add()
		elif num == 2:
			change()
		elif num == 3:
			pass
		elif num == 4:
			pass
		elif num == 0:
			print('谢谢使用！')
			exit()
def add():
	d = {}
	book_name = input('请输入书名：')
	d['book_name'] = book_name
	name = input('请输入作者名:')
	d['name'] = name
	price = input('请输入价目：')
	d['price'] = price
	date = input('请输入入库日期：')
	d['date'] = date
	book_num = input('请输入书号：')
	d['book_num'] = book_num
	list.append(d)
	print('添加成功')

def change():#修改功能
	book_name = input('请输入书名：')
	for d in list:
		if d['book_name'] == book_name:
			print('0:返    回')
			print('1:修改书名')
			print('2:修改作者')
			print('3:修改价目')
			print('4:修改日期')
			print('5:修改书号')
			change_1()
		else:
			('没有此书')

def change_1():
	num = input('请选择功能：')
	for d in list:
		if isNum(num):
			num = int(num)
		if num == 0:
			showMenu()
		if num == 1:
			book_name = input('请输入新的书名：')
			d['book_name'] = book_name
		if num == 2:
			name = input('请输入新的作者：')
			d['name'] = name
		if num == 3:
			price = input('请输入新价目：')
			d['price'] = price
		if num == 4:
			book_num = input('请输入新的书号：')
			d['book_num'] = book_num
		list.append(d)
		print(list)

login()
