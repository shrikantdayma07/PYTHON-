#reduce functions : whenever we want the multiple additions from the sequences then we go for reduce functions 
l=[1,2,3,4,5,6,7,8,9,10]
from functools import reduce
s = reduce(lambda x,y: x + y,l)
print(s)