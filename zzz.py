list = []#空列表存放图书
account = 'library'
password = 'a12345'

def fenge():
	print('-'*50)

def isNum(num):#判断是否为纯数字
	if num.isdigit():
		return True
	else:
		return False

def isError(msg):
	print(msg+'格式有误，请重新输入！')

def bookname():
	for d in list:
		print(d['book_name'])

def login():#登录界面
	print('*'*50)
	print('欢迎来到图书管理系统'.center(40,' '))#center居中左右空格补冲
	for i in range(3):
		acc = input('请输入账号：'.rjust(21,' '))
		pas = input('请输入密码：'.rjust(21,' '))
		if acc == account and pas == password:
			print('')
			print('...登录成功'.rjust(45,' '))
			showMenu()
			break
		else:
			print('账号或密码错误！'.rjust(23,' '))
			print(('您还有%d次机会'%(2-i)).rjust(22,' '))
			fenge()

def showMenu():#功能菜单
	print('-'*50)
	print('0:退  出  系  统'.center(45,' '))
	print('1:增  加  图  书'.center(46,' '))
	print('2:修  改  图  书'.center(45,' '))
	print('3:查  找  图  书'.center(45,' '))
	print('4:删  除  图  书'.center(46,' '))
	print('5:打  印  图  书'.center(46,' '))
	fenge()
	input_info()

def add():
	d = {}#空字典存图书信息
	book_name = input('请输入书名：')
	d['book_name'] = book_name
	name = input('请输入作者名:')
	d['name'] = name
	while True:
		price = input('请输入价目(元)：')
		if isNum(price):
			price = float(price)
			d['price'] = price
			break
		else:
			isError('价目')
	while True:
		date = input('请输入入库日期：')
		if isNum(date):
			date = int(date)
			d['date'] = date
			break
		else:
			isError('日期')
	while True:
		book_num = input('请输入书号：')
		if isNum(book_num):
			book_num = int(book_num)
			d['book_num'] = book_num
			break
		else:
			isError('书号')
	list.append(d)
	print('添加成功')
	print(list)
	fenge()

def change_menu():#修改功能菜单
	print('0:返回菜单\n1:修改书名\n2:修改作者\n3:修改价目\n4:修改日期\n5:修改书号')
		
def change():
	bookname()
	name = input('请输入书名：')
	for d in list:
		if d['book_name'] == name:
			change_menu()
			while True:
				num = input('请选修改项：')
				if isNum(num):
					num = int(num)
					if num == 0:
						showMenu()
					elif num == 1:
						name = input('请输入新的书名：')
						d['book_name'] = name
					elif num == 2:
						name = input('请输入新的作者：')
						d['name'] = name
					elif num == 3:
						price = input('请输入新的价目：')
						if isNum(price):
							price = float(price)
							d['prcie'] = price
						else:
							isError('价目')
					elif num == 4:
						date = input('请输入新的日期：')
						if isNum(date):
							date = int(date)
							d['date'] = date
						else:
							isError('日期')
					elif num == 5:
						b_num = input('请输入新的书号：')
						if isNum(b_num):
							b_num = int(b_num)
							d['book_num'] = b_num
							
						else:
							isError('书号')
					print('修改成功')
def find():
	bookname()
	name = input('请输入书名：')
	for d in list:
		if d['book_name'] == name:
			print('书名： %s\n作者： %s\n价目： %s\n书号： %s'%(d['book_name'],d['name'],d['price'],d['book_num']))
			break

def delete():
	bookname()
	name = input('请输入书名：')
	for d in list:
		if d['book_name'] == name:
			list.remove(d)
			print('删除成功')
			break

def print_book():
	print('书名        作者        价目        日期         书号         ')
	for d in list:
		print(d['book_name'],end = '        ')
		print(d['name'],end = '        ')
		print(d['price'],end = '        ')
		print(d['date'],end = '        ')
		print(d['book_num'],end = '        ')
		print('')

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
			#pass
		elif num == 3:
			find()
			#pass
		elif num == 4:
			delete()
			#pass
		elif num == 5:
			print_book()
			#pass
		elif num == 0:
			print('谢谢使用！\n欢迎下次光临！')
			exit()

login()
