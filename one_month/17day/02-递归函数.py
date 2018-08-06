'''
def test(num):
	if num == 1:
		return num
	else:
		return num*test(num-1)
ret = test(5)
print(ret)
'''

def test1(num):
	if num == 1:
		return num
	else:
		return num+test1(num-1)
ret = test1(100)
print(ret)
