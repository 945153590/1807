import time
list = []
money = 0 #收益
ctime = 0 #入住时间
etime = 0 #离店时间
a = 0 #入住人数统计
b = 0 #离店人数统计
def showMenu():
	while True:
		print('欢迎来到宾馆入住系统')
		print('1:入住')
		print('2:离店')
		print('3:统计')
		print('4:退出')
		sec()	

def sec():
	sect = int(input('请选择功能：'))
	if sect == 1:
		add()
	elif sect == 2:
		delete()
	elif sect == 3:
		tongji()
	elif sect == 4:
		print('谢谢使用')
		exit()
	
def add():
	global ctime
	global a
	d = {}
	name = input('请输入姓名：')
	d['name'] = name
	while True:
		id_card = input('请输入身份证号：')
		if len(id_card) == 18:
			d['id_card'] = id_card
			print('登记成功')
			a+=1
			break
		else:
			print('号码不是18位请重新输入')
	ctime = int(time.time())
	d['ctime'] = ctime
	list.append(d)
	print(list)

def delete():
	global etime
	global b
	name1 = input('请输入姓名：')
	for d in list:
		print(d)
		if d['name'] == name1:
			list.remove(d)
			print('成功离店')
			etime = int(time.time())
			b+=1
		else:
			print('没有此人')

def tongji():
	money = (etime - ctime) * 10
	print('今天收益%.02f元,总入住人数为%d，离店人数为%d'%(money,a,b))
	
showMenu()
