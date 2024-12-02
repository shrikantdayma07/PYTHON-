#loop inside loop is called as Nested loop, here we use for loop two times for inner as well as outer loop - i,j

#here we will se the nested loop example in python
'''for i in range(5):
    for j in range(5):
        print(i,j,end=" ") #this end=" " will help us to print the 1st iteration in one line and next iteration in another line 
    print("\n")'''

#this code will print the stars pattern
'''for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()'''

#this code will print the numbers from 1 to 15
'''a=1
for i in range(1,6):
    for j in range(i):
        print(a ,end =" ")
        a+=1
    print()'''

#actual logic of stars in python in simple way
'''for i in range(1,6):
    print(i * '*', '')'''

#this will print the solid rectangle using the nested loop 
'''for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()'''

#this code help us to find the stars pattern in the reverse order 
'''n=4
for i in range(1,6):
    for j in range(i):
        print(" ", end="")
    for j in range(n - i + 1):
        print("*",end="")
    i+=1
    print()'''
    
#traingle pattern in proper order 
'''for i in range(1,6):
    for j in range(i):
        print("*", end = " ")
        i+=1
    print()'''
    
#print the pattern of even numbers incrementing by 2
'''num = 0
for i in range(1,5):
    for j in range(i):
        print(num, end=" ")
        num+=2
    print()'''
    
#print the numbers using multiple of 2
'''num = 2
for i in range(1,5):
    for j in range(i):
        print(num, end = " ")
    num *= 2 #this is placed outside the loop so that it multiplies the num by 2 and if we are writing this inside inner loop which multiplies the previous output 
    print()'''
    
#pattern to print the lowercase character 
index = 97
for i in range(1,5):
    for j in range(i):
        print(chr(index),end=" ")
        index += 1
    print()

#next pattern to print the characters       
'''index=97
for i in range(1,5):
    for j in range(i):
        print(chr(index),end=" ")
    index += 1
    print()'''
    
