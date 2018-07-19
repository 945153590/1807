import random
for i in range(10):
	a = random.randint(1,3)
	b = int(input('1：石头，2：剪刀，3：布'))
	if b == 1 and a == 2 or b == 2 and a == 3 or b == 3 and a == 1:
		if i < 3:
			print('这是油加满的效果!!')
		if i < 5 and i >= 3:
			print('油用了三分之一的效果。')
		print('player win')
		break
	if b == 1 and a == 3 or b == 2 and a == 1 or b == 3 and a == 2:
		print('pc win')
		print('电脑都玩不过，你需要加油了！！')
	if a == b:
		print('ping')
		print('怎么能打成平手呢，这不是你的风格啊')
