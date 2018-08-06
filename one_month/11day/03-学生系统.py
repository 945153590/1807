students = []
ac = 'xiaotian'
pas = 123456
print('#'*50)
print('欢迎来到学生管理系统')
print('*'*50)
for ii in range(3):
	ac1 = input('请输入账号：')
	pas1 = int(input('请输入密码：'))
	if ac1 != ac or pas1 != pas:
		print('账号或密码错误,请重新输入\n您还有%d次机会'%(3-ii-1))
	elif ac1 == ac and pas1 == pas:
		print('-'*50)
		while True:
			print('1:添加学生')
			print('2:查找学生')
			print('3:修改学生')
			print('4:删除学生')
			print('5:打印学生')
			print('6:退出系统')
			num = int(input('请选择功能:'))
			print('-'*50)
			if num == 1:
				d = {}
				name = input('请输入学生姓名：')
				age = int(input('请输入年龄：'))
				sex = input('请输入性别：')
				phone = int(input('请输入联系方式：'))
				phone1 = int(input('请输入紧急联系人方式：'))
				addr = input('请输入家庭住址：')
				addr1 = input('请输入籍贯：')
				print('-'*50)
				d['name'] = name
				d['age'] = age
				d['sex'] = sex
				d['phone'] = phone
				d['phone1'] = phone1
				d['addr'] = addr
				d['addr1'] = addr1
				students.append(d)
				print(students)
				print('-'*50)	
			elif num == 2:
				print('查找学生：')
				name = input('请输入姓名：')
				for d in students:
					if d['name'] == name:
						print('学生姓名：%s\n学生年龄：%d\n学生性别：%s\n学生电话：%d\n学生紧急联系人电话：%d\n学生住址：%s\n学生籍贯：%s'%(d['name'],d['age'],d['sex'],d['phone'],d['phone1'],d['addr'],d['addr1']))
						break
					else:
						print('查无此人')
			elif num == 3:
				print('修改学生:')
				name = input('请输入要修改学生姓名:')
				for d in students:
					if d['name'] == name:
						print('学生姓名：%s\n学生年龄：%d\n学生性别：%s\n学生电话：%d\n学生紧急联系人电话：%d\n学生住址：%s\n学生籍贯：%s'%(d['name'],d['age'],d['sex'],d['phone'],d['phone1'],d['addr'],d['addr1']))
						print('-'*50)
						print('0:保存并返回')
						print('1:修改名字')
						print('2:修改年龄')
						print('3:修改性别')
						print('4:修改电话')
						print('5:修改紧急联系人电话')
						print('6:修改学生住址')
						print('7:修改籍贯')
						print('-'*50)
						while True:
							num = int(input('请输入修改序号：'))
							if num == 1:
								name = input('请输入新名字：')
								d['name'] = name
							elif num == 2:
								age = int(input('请输入新的年龄：'))
								d['age'] = age
							elif num == 3:
								sex = input('请输入新的性别：')
								d['sex'] = sex
							elif num == 4:
								phone = int(input('请输入新的电话：'))
								d['phone'] = phone
							elif num == 5:
								phone1 == int(input('请输入紧急联系人新号码：'))
								d['phon1'] = phone1
							elif num == 6:
								addr = input('请输入新的家庭住址：')
								d['addr'] = addr
							elif num == 7:
								addr1 = input('请输入新的籍贯：')
								d['addr1'] = addr1
							print('修改成功')
							print('-'*50)
							if num == 0:
								break
			elif num == 4:
				print('删除学生:')
				name = input('请输入要移除的学生姓名：')
				for d in students:
					if d['name'] == name:
						students.remove(d)
						print('删除成功')
						break
				print('-'*50)
			elif num == 5:
				print('姓名        年龄        性别        电话        紧急联系人   住址        籍贯')
				for d in students:
					print(d['name'], end = '        ')
					print(d['age'],end = '        ')
					print(d['sex'],end = '        ')
					print(d['phone'],end ='        ')
					print(d['phone1'],end = '        ')
					print(d['addr'],end = '        ')
					print(d['addr1'],end = '        ')
					print('')	
			elif num == 6:
				print('谢谢使用!!!')
				break
		break
print('*'*50)
