d = {'name':'laotian','sex':'男','birthday':'1000年10月10日','address':'hebei'}
print(d)
d['name'] = '田晓东'
print(d)
d.pop('address')
print(d)
d['address'] = '河北'
print(d)
print(d['name'])
'''
for i in d:
	print(i)
	print(d[i])
'''
'''
for j in d.keys():
	print(j)
	print(d[j])
'''
'''
for k in d.values():
	print(k)
'''
'''
for l,m in d.items():
	print(l)
	print(m)
'''
for i in d.items():
	print(i)
	print(i[0])
	print(i[1])
print(len(d))



