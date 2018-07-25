def test(a,*args,b=12,**kwargs):
	sum = 0
	sum = sum + a
	for i in args:
		sum = sum + i
	for v in kwargs.values():
		sum = sum + v
	sum = sum + b
	return sum	
ret = test(1,2,3,4,5,b=20,m=12,n=22)
print(ret)
