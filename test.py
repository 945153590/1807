list = []
ac = 'students'
pas = 123456
print('*'*50)
print('欢迎来到学生管理系统')
print('-'*50)
for i in range(3):
	ac1 = input('请输入账号：')
	pas1 = int(input('请输入密码：'))
	if ac == ac1 and pas == pas1:
		print('登录成功')
		print('-'*50)
		while True:
			print('请选择功能')
			print('0:退出系统')
			print('1:添加学生')
			print('2:查找学生')
			print('3:修改学生')
			print('4:删除学生')
			print('5:打印学生')
			print('-'*50)
			d = {}
			a = int(input('请选择功能：'))
			if a == 1:
				name = input('请输入姓名：')
				d['name'] = name
				age = int(input('请输入年龄：'))
				d['age'] = age
				sex = input('请输入性别：')
				d['sex'] = sex
				list.append(d)
				print(d)
				print(list)
			elif a == 2:
				name = input('请输入姓名：')
				for d in list:
					if d['name'] == name:
						print('学生姓名：%s\n学生年龄%d\n学生性别:%s'%(d['name'],d['age'],d['sex']))
						break
					if d['name'] != name:
						print('查无此人')
			elif a == 3:
				name = input('请输入姓名：')
				for d in list:
					if d['name'] == name:
						print('学生姓名：%s\n学生年龄%d\n学生性别:%s'%(d['name'],d['age'],d['sex']))
						print('-'*50)
						print('0:保存和退出,1:修改姓名,2：修改年龄,3：修改性别')
						print('-'*50)
						while True:
							num = int(input('请选择功能：'))
							if num == 1:
								name = input('请输入新的姓名：')
								d['name'] = name
							elif num == 2:
								age = int(input('请输入新的年龄：'))
								d['age'] = age
							elif num == 3:
								sex = input('请输入新的性别：')
								d['sex'] = sex
							elif num == 0:
								print('ok')
								break
			elif a == 4:
				name = input('请输入姓名：')
				for d in list:
					if d['name'] == name:
						list.remove(d)
						print('删除成功')
						break
			elif a == 5:
				print('name        age        sex        ')
				for d in list:
					print(d['name'],end = '        ')
					print(d['age'],end = '        ')
					print(d['sex'],end = '        ')
					print('')
			elif a == 0:
				print('谢谢使用')
				break
			else:
				print('无效选择')
		break
	if ac != ac1 or pas !=pas1:
		print('账号或密码错误\n您还有%d次机会'%(2-i))
	




