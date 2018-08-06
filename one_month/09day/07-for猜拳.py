import random
#1--石头
#2--剪刀
#3--布
for i in range(10):
	pc = random.randint(1,3)
	py = int(input('请输入1：石头，2：剪刀，3：布：'))
	if py == 1 and pc == 2 or py == 2 and pc == 3 or py == 3 and pc == 1:
		print('玩家win')
		break
	elif py == pc:
		print('平手')
	else:
		print('电脑win')
	
