list=[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}]
for i in list:
	for j,m in i.items():
		for k,v in m.items():
			print(j,k,v)
