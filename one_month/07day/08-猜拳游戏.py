ply = int(input('请出拳 1：石头 2：剪刀 3：布:'))
import random
pc = random.randint(1,3)
if ply < 4 and ply > 0:
	if (ply == 1 and pc == 2) or (ply == 2 and pc == 3) or (ply == 3 and pcc == 1):
		print('player win')
	elif ply == pc:
		print('平局')
	else:
		print('pc win')
else:
	print('非法操作')
