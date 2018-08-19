'''
class dogs():
    def jiao(self,name):
        if name == 'erha':
            print('汪汪叫')
        else:
            print('狂叫')
    def eat(self,name):
        if name == 'erha':
            print('吃狗粮')
        else:
            print('吃二氧化碳')

erha = dogs()
erha.jiao('erha')
erha.eat('erha')

xiaotianquan = dogs()
xiaotianquan.jiao('xiaotianquan')
xiaotianquan.eat('xiaotianquan')
'''

class dogs():

	def jiao(self,jiaos):
		print('%s叫的方法%s'%jiaos)

	def eat(self,food):
		print('吃%s'%food)

hsq = dogs()
hsq.jiao('汪汪汪')
hsq.eat('狗粮')

xtq = dogs()
xtq.jiao('狂叫')
xtq.eat('二氧化碳')
