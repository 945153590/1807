print('/'*50)
account = input('请输入您的账号')
password = input('请输入您的密码')
nick_name = input('请输入您的姓名')
money = 200000#原有存款
need_money = input('请输入您要提取的金额')
sum = (money - int(need_money))
print('/'*50)
print('账号：%s\n密码%s\n姓名%s\n原有金额%s\n取款金额%s\n剩余%s'%(account,password,nick_name,money,need_money,sum))

