def s(start,end):#声明函数  end是一个形参
	sum = 0
	for i in range(start,end+1):
		sum=sum+i
	print(sum)
start = int(input('请输入起始值'))
end = int(input('请输入终止值'))
s(start,end)#调用函数
