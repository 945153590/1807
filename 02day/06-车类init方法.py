class car():
	#初始化属性
	def __init__(self,color,type):#魔法方法 实例化方法
		self.color = color
		self.type = type

	def __str__(self):
		msg = '我的颜色是%s,我的类型是%s'%(self.color,self.type)
		return msg

	def move(self):
		print('移动')

	def music(self):
		print('听音乐')
	
BMW = car('蓝色','超跑')#创建对象或创建一个实例
BMW.move()
BMW.music()
print(BMW)
