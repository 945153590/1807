print('——'*30)
print('\t\t东家便利店收银系统')
print('*'*60)
account = input('\t\t请输入您的账号:')
password = input('\t\t请输入您的密码:')
print('*'*60)
'''
商品名称=name
商品价格=price
商品重量=weight
'''
name = ('\ta:橙子|b:油桃|c:香蕉|d:苹果|e:橘子|f:葡萄|g:梨')
print(name)
price = ('\t1.2元 |2.3元 |0.9元 |5.8元 |1.3元 |2.4元 |3.3元')
print(price)
print('*'*60)
x = input('请输入水果价格：')
y = float(input('请输入水果重量：'))
print('价格:%.02f'%(float(x)*y))
print('——'*30)
