#WAP to remove duplicate from the list 
l=[1,2,34,5,61,2,4,62,5,2,34]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)