def test(a,b = 100):
	sum = 0
	for i in range(b+1):
		sum = sum + i
	return sum
ret = test(1)
print(ret)

