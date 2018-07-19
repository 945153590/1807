a = ['xiaozhao','xiaoqian','xiaosun']
for i in a:
	print(i)
a.append('xiaoli')
print(a)
a.insert(1,'xiaozhou')
print(a)
a.extend('xiaowu')
print(a)
b = ['xiaotian','xiaoluo']
a.append(b)
print(a)
a.insert(0,b)
print(a)
a.extend(b)
print(a)
