dream = []
where = ['中国','日本','法国']
fj = ['西湖','富士山','埃菲尔铁塔']
lan = ['chinese','japen','france']
dream.append(where)
#print(dream)
#dream.extend(lan)
#print(dream)
dream.insert(0,fj)
print(dream)
for i in dream:
	print(i)
	for j in i:
		print(j)
