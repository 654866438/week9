
#要写一个排列函数
#给定一个列表，把偶元素按从0到n / 2的降序重新排列
#（基于索引顺序）排列，奇元素按从（n / 2）+1到n的升序排列。
def arrange(s):	
   s1 = s[:]
   n = len(s) - 1
   if n % 2 == 1: #初始化最后的奇元素和偶元素
       even = n - 1
       odd = n - 2
   else:
       even = n
       odd = n - 1
   k = 0
   for i in range(even,-1,-2): #array的前半部分按降序排列
       s[k] = s1[i]
       k += 1
   for i in range(1,odd+1,2): #array的后半部分按升序排列
       s[k] = s1[i]
       k += 1
   pass #不再有权访问原始列表内容
	
