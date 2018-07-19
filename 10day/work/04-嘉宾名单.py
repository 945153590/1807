names = ['啊宽','老张','小吴','小凯']
for i in names:
	print('%s,来房山共进晚宴'%i)
print('%s,不能来参加晚宴'%(names[0]))
names[0] = '津津'
for j in names:
	print('%s,来房山参加晚宴'%j)
print('我找到一个更大的餐桌')
names.insert(0,'小房')
names.insert(3,'小路')
names.append('小王')
print(names)
for k in names:
	print('亲爱的%s,我将邀请您参加周六晚上的晚宴，地点在你家！'%k)
print('各位亲，由于我定的餐桌不能及时送达，所以只能邀请两位，非常抱歉')
print(len(names))
names.pop(0)
print('%s非常抱歉，无法邀请您来参加晚宴'%(names[0]))
names.pop(0)
print('%s非常抱歉，无法邀请您来参加晚宴'%(names[0]))
names.pop(0)
print('%s非常抱歉，无法邀请您来参加晚宴'%(names[0]))
names.pop(0)
print('%s非常抱歉，无法邀请您来参加晚宴'%(names[0]))
names.pop(0)
print('%s非常抱歉，无法邀请您来参加晚宴'%(names[0]))
print(names)
for i in names:
	print('%s,您仍在受邀之列'%i)
del names[0:2]
print(names)
