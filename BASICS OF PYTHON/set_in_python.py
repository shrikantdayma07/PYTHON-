#in python when set is defined and if we insert the duplicates value, it will remove that duplicates value and return only the unique values
# s={1,2,3,4,5,3,2,4,5,1,2,3}
# print(s)
# print(type(s))

#output of the above is : {1, 2, 3, 4, 5}
#<class 'set'>

#s={1,2,3,5,4,2,1,4,3} #this is called as set() method or set() constructor which is used to print empty set 
# set1=set()
# print(type(set1)) 

#in set the data is stored in the random order i.e. the data can be come anywhere no matter what the sequence is 
# set1=(1,2,"Python",4.5)
# print(set1)

#important functions in the set 
#1] len() it is used to calculate length of the set
#2] add() : it is used to add element at random(arbitrary) position
# set1={1,2,3,"Python",4}
# set1.add(5)
# print(set1)

#3] remove() : it is used to remove any element from the set
# set1={1,2,3,"Python",4,5}
# set1.remove(5)
# print(set1)

#4] update() : it is used to add iterable object like string, int , etc. multiple element ..!!
#in update() we cannot add individual element 
# set1={1,2,3,"Python",4,5}
# set1.update(range(51,55)) #it will add element upto only 54th element 
# print(set1)

#5] copy() : it is used to return copy of the set 
#it is cloned object 

# s={10,20,30}
# s1=s.copy()
# print(s1)

#6] Pop() : it removes and returns some random element from the set 
# s={10,20,30}
# print(s.pop())
# print(s.pop())
# print(s.pop())

#7] remove() : it removes specified element from the set --->> it gives the error 
# s={40,10,30,20}
# s.remove(30)
# print(s)

#8] discard() : it removes the specified element from the set 
#if the specified element not present still it will not give the error 

#9] clear() : to remove all elements from the set 
# s={10,20,30}
# print(s)
# s.clear()
# print(s)

#Mathematical operations on the Set: 

#1. Union() : we can use this function to return all elements present in both sets 

# x={10,20,30,40}
# y={30,40,50,60}
# print(x.union(y))
# print(x|y)

#2. intersection() : it returns common element present in both x and y 
# x={10,20,30}
# y={40,50,20}
# print(x.intersection(y))
# print(x&y)

#3. difference() : returns the elements present in x but not in y
# x={10,20,30}
# y={40,50,20}
# print(x.difference(y))
# print(x-y)
# print(y-x)

#this symmetric difference will remove the common element from both the sets 
# x={10,20,30,40}
# y={30,40,50,60}
# print(x.symmetric_difference(y))  #here 30,40  is removed from the set!!
# print(x^y)

#set comprehension : it is applicable in the python --->> it is possible in python
# s={x*x for x in range(5)}
# print(s)

#program to print the even numbers from a given set using set comprehension 
s={1,2,3,4,5,6,7,8,9,10}
s1={i for i in s if i % 2 == 0}
print(s1)


#in set -->> difference between pop and remove is : when we used pop any random element can be removed but in remove particular element is removed itself whichever we mentioned 