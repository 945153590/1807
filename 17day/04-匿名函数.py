def heihei(x,y,z):
	ret = z(x,y)
	return ret
	
ret = heihei(5,80,lambda x,y:x*y)
print(ret)
