list = [{'book_name':'python'},{'book_name':'python2'}]
name = input('请输入书名：')
flag = 1
for d in list:
	if d['book_name'] == name:
		while True:
			num = int(input('请选修改项：'))
			if num == 1:
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
	else:
		print('没有找到此书')
