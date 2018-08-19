class cfkjb():
	def gongshi(self):
		for i in range(1,10):
			for j in range(1,i+1):
				print('%d*%d=%d'%(j,i,j*i),end = ' ')
			print('')
koujue = cfkjb()
koujue.gongshi()
