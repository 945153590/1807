import random
for i in range(3):
	a = random.randint(1,3)
	pl = int(input('请选择1：石头，2：剪刀，3：布'))
	if pl == 1 and a == 2 or pl == 2 and a == 3 or pl == 3 and a == 1:
		print('pl win')
	elif pl == 1 and a == 3 or pl == 2 and a == 1 or pl == 3 and a == 3:
		print('a win')
	elif a == pl:
		print('ping')

