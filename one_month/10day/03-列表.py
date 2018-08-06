#list
home = ['xiaozhao','xiaoqian','xiaoli',1,3.3,True]#定义一个列表
#添加
home1 = ['xiaozhao','xiaohe','xiaohu']
home1.append('laosong')#老宋进home1，按顺序添加
print(home1)

home1.insert(0,'老宋')#可以设置添加位置
print(home1)

#删除
home1.pop()#删除最后面内容
print(home1)

home1.pop(0)#谁在0号位删除0号位的内容
print(home1)

home1.remove('xiaohu')#根据名字删
print(home1)



