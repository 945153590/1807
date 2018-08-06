'''
i = 0
while i < 8:#控制打印排数
	j = 0
	while j < 4:#控制每排中有多少人
		print('*',end='')#打印每排的人数，不换行
		j+=1
	print('')#换行
	i+=1

#乘法口诀
sum = 0
i = 1
while i < 10:
	j = 1
	while j <= i:
		sum = i*j
		print('%d×%d=%d '%(j,i,sum),end='')
		j+=1
	print('')
	i+=1
'''
#直角三角形
i = 0#i相当于打印*的排数
while i < 6:#排数不能超过6排,也就是打印5排
	j = 1#j相当于每排有几个*
	while j <= i:#列的数量不能超过排的数量
		print('*',end=' ')#打印*不换行
		j+=1
	print('')#换行打印
	i+=1







