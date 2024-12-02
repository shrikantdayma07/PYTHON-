#print(range(11))

'''For Loop in Python '''

#this program will print the values from 0 to 10
'''for i in range (0,11,1):
    print(i) '''

#this program will print values from 1 to 10
''' for i in range (1,11,1):
    print(i) '''

#this program will print values from 1 to 100
'''for i in range (1,101,1):
    print(i)'''

#this program will print even values from 0 to 100
'''for i in range (0,101):
    if(i%2==0):
        print(i)'''

#this program will print the odd values from to 100
'''for i in range (0,101):
    if(i%2!=0):
        print(i)'''

#this program will print the prime number and take input from the user
'''number = int(input("Enter an integer number: "))
for i in range (2,number):
    if number % i == 0:
        print('not prime')
        break
else:
    print ('Prime')'''

#number to print even number count between 0 to 10
'''count=0
for i in range (0,11):
    if i%2==0:
        count = count+1 #using assignment operator, we can count count += 1
print(count) '''
 
#number to print odd number count between 0 to 100
'''count = 0
for i in range (0,101):
    if i%2!=0:
        count = count + 1
print(count) '''

#number to check prime number a/c to sir's logic
'''c=0
num=int(input("Enter an integer number : "))
for i in range (1,num+1):
    if num % i ==  0:
        c+=1
if c==2:
    print('prime')
else:
    print('not prime') '''

#number to check prime number by another logic
count=0
num=int(input("Enter an integer number : "))
for i in range(2,num+1):
    if num%i==0:
        count+=1
if count==1:
    print('prime')
else:
    print('not prime') 


#to determine the time complexity 
'''c=0
num=int(input("Enter an integer number : "))
for i in range (2,num+1//2):
    if num % i ==  0:
        c+=1
if c==0:
    print('prime')
else:
    print('not prime') '''
    



    
