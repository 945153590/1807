students = ()
ac = 'xiaotian'
pas = 123456

print('欢迎来到学生管理系统')
ac1 = input('请输入账号：')
pas1 = int(input('请输入密码：'))
if ac1 == ac and pas1 == pas:
	print('1:添加学生')
	print('2:查找学生')
	print('3:修改学生')
	print('4:删除学生')
	print('5:退出系统')
	num = int(input('请选择功能'))
	if num == 1:
		d = {}
		name = input('请输入学生姓名：')
		age = int(input('请输入年龄：'))
		sex = input('请输入性别：')
		phone = int(input('请输入联系方式：'))
		phone1 = int(input('请输入紧急联系人方式：'))
		addr = input('请输入家庭住址：')
		addr1 = input('请输入籍贯：')
		d['name'] = name
		d['age'] = age
		d['sex'] = sex
		d['phone'] = phone
		d['phone1'] = phone1
		d['addr'] = addr
		d['addr1'] = addr1
		print(d)
