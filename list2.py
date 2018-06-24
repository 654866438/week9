
#要写一个排列函数
#给定一个列表，把偶元素按从0到n / 2的降序重新排列
#（基于索引顺序）排列，奇元素按从（n / 2）+1到n的升序排列。

def arrange(lst):
	result = []
	
	first = len(lst)-1
	
	if first%2 == 1:
                
		first = first - 1
		
	for i in range(first, -1, -2):
                
		result.append(lst[i])
		
	for i in range(1, len(lst), 2):
                
		result.append(lst[i])
		
	lst = result
	print(lst)
