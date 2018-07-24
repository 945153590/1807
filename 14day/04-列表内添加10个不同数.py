'''
def nums():
	import random
	list = []
	for i in range(10):
		n = random.randint(1,100)
		if n not in list:
			list.append(n)
	print(list)
nums()
'''


def nums():
	import random
	list = []
	while True:
		num = random.randint(1,100)
		if num not in list:
			list.append(num)
			if len(list) == 10:
				print(list)
				break
nums()
