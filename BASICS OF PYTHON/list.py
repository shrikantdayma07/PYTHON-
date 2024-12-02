#list : a collection of dissimilar datatypes i.e. any datatype can be their in the list like string, int , float or negative numbers 
#list is mutable this means once defined the list you can change it 
# l=[1,0.5,-5,'Shrikant']
# print(l)          #[1, 0.5, -5, 'Shrikant']
# print(type(l))    #<class 'list'>

#to calculate the length of this list 
# n=len(l)
# print("Total no. of elements in the list: ",n)     #Total no. of elements in the list:  4

#accessing list elements 
# l1=[10,89.7,-3,45.6,'ITVEDANT']
# print(l1[3])   #45.6
# print(l1[-4])  #89.7

#slicing in list 
# l=[10,89.7,-3,45.6,'ITVEDANT']
# l1=l[1:4:1]
# print(l1)      #[89.7, -3, 45.6]

# rev = l[::-1]
# print(rev)

#for loop over list 
# l=[10,89.7,-3,45.6,'ITVEDANT']
# print("with index")
# for i in range(0,len(l),1):
#     print(l[i])

# print("Without index")
# for i in l:
#     print(i)

#add element in the list
#append() function
# l=[10,89.7,-3,45.6,'ITVEDANT']
# l.append(24.5)
# print(l)

# l.append('Shrikant')
# print(l)

#insert() function
# l=[10,89.7,-3,45.6,'ITVEDANT',24.5,'Shrikant']
# l.insert(3,50)
# print(l)      #[10, 89.7, -3, 50, 45.6, 'ITVEDANT', 24.5, 'Shrikant']

#update the element in the list
# l=[10, 89.7, -3, 45.6, 'ITVEDANT', 24.5, 'Shrikant']
# l[4]="ITVEDANT-eclass"
# print(l)

#delete or remove the list elements
# l=[10, 89.7, -3, 50, 45.6, 'ITVEDANT-eclass', 24.5, 'Shrikant']
# l.pop()
# print(l)

# l.pop(2)
# print(l)

#del() : it is a keyword which is used to delete the entire list 
# l=[10, 89.7, -3, 50, 45.6, 'ITVEDANT-eclass', 24.5, 'Shrikant']
# del l
# print(l)

#write a program to find summation of the integer element in the list 
# l=[10,20,35,1,2,-3]
# total=0
# for x in l:
#     total = total + x
# print("Summation is: ",total)

#a program to filter positive and negative elements separately from the list 
l=[1,-9,89,76,-56,-3,0,12,15,167,-8,2]
lpos = []
lneg = list()   #lneg = [] this could also be work as expected as this list() is simple the blank list 
for x in l:
    if x>0:
        lpos.append(x)
    else:
        lneg.append(x)
print("Positive list: ",lpos)
print("Negative list: ",lneg)

#a program to find maximum number from the list 
# my_list = [1,2,3,4,5]
# max_num = max(my_list)
# print(max_num)