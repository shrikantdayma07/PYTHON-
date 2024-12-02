#Built-in function in Python !!

'''difference between append and insert 
difference between remove and pop  '''

'''list2 = (1,2,3,4,5,6,7,8)
print(list2)'''

#count() : it is used to count the number of elements present in the list 
# list1=[1,2,2,5,4,6,2,1,4,5,3,6,8,7,2]
# print(list1.count(2))

#append() : used to add element at the end of the list 
# list3=[1,2,3,4,5,6,7,8,9]
# list3.append(10)
# print(list3)

#insert() : used to add element at the specific position 
#syntax : list.insert(position(index value), element)

# list2 = [1,2,3,4,5,6,7,8]
# list2.insert(3,50)
# print(list2)

#extend() : add list into another list 
#syntax : list1.extend(list2)

# l1=[1,2,3]
# l2=[4,"HELLO",6]
# l1.extend(l2)
# print(l1)

#pop() : it is used to return and remove last element of the list 
# print(l1.pop())
# print(l1)
# print(l1.pop())
# print(l1)

#remove() : it is used to remove the specific element from the list 
# l1.remove(3) #it will remove the element 3 from the list given above 
# print(l1)

#reverse() : it is used to reverse order of the element present in the list
# list4=[1,2,3,4,5]
# list4.reverse()
# print(list4)

#sort() : used to sort the list element in ascending and descending order 
#list.sort()

# list4.sort()
# print(list4)

# list4.sort(reverse=True) #this is used when we want the list in the descending order !!
# print(list4)

my_list=[10,20,30,40]
ur_list=my_list #[10,20,30,40]
print(id(my_list))
print(id(ur_list))

#cloning : exactly duplicate 