'''
class bingxiang():
	def opendoor(self):
		print('开门')
	def zhuangdaxiang(self):
		print('装大象')
	def closedoor(self):
		print('关门')
haier = bingxiang()
haier.opendoor()
haier.zhuangdaxiang()
haier.closedoor()
'''

class person():

	def goshopping(self):
		print('去商店')

	def buy(self):
		print('购物')

	def gohome(self):
		print('回家')

	def introduce(self):
		print('我的年龄是%d 我的身高是%d'%(self.age,self.height))

woman = person()
woman.goshopping()
woman.buy()
woman.gohome()
woman.age = 22
woman.height = 170
woman.introduce()

man = person()
man.goshopping()
man.buy()
man.gohome()
man.age = 24
man.height = 180
man.introduce()
