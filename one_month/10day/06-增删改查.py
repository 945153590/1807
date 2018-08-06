#coding=utf-8
name = ['xiaotian','xiaoli','xiaozhang']
name.append('小刘')
print(name)
name.insert(1,'小鹏')
print(name)
name.remove('xiaotian')
print(name)
name.pop()
print(name)
name.pop(2)
print(name)
name1 = ['hhh']
name.extend(name1)
print(name)
#查找
print(name[0])#查找0号
#修改
name[2] = 'ahuang'
print(name)
