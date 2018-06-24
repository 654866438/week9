
#要写一个排列函数
#给定一个列表，把偶元素按从0到n / 2的降序重新排列
#（基于索引顺序）排列，奇元素按从（n / 2）+1到n的升序排列。

def arrange(input):
	even =[]
	odd=[]
	for i in reversed(range(0,len(input))):
                if(i%2==0):
                        even.append(input[i])
			for i in range(0,len(input)):
				if(i%2!=0):
					odd.append(input[i])
					print(even+odd)
					list = [1,2,3,4,5]
					arrange(list)
