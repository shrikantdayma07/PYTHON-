#if the value is true then it will execute the if block, otherwise it will execute the else block 
''' a=5
if(a>5):
    print(' A is greater than 5')
else:
    print('A is less than 5') '''

''' a=10
if(a%2==0):
    print('a is even number')
else:
    print('a is not an even number') '''


#if you are not giving the datatype as "int" then it will consider as string, so you have to always mention
#code to check whether a number is even or odd
#take input from the user
''' a=int(input("Enter an integer number: "))
if(a % 2 == 0):
    print("The number is even")
else:
    print("The number is odd") '''

#program to take age as an input from the user and check whether he/she is eligible for voting or not ?
'''age=int(input("Enter your age: "))
if(age>=18):
     print("The person is eligible for voting")
else:
    print("The person is not eligible for voting")'''



#if - elif statements
#it is used when we have to execute multiple statements 
'''a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if(a>b and a>c ):
    print("a is greater than b and c")
elif(b>c and b>a):
    print("b is greater than a and c")
else:
    print("c is greater than a and b") '''


#take input from user (1 to 7) and accordingly print day which comes under the week 
a=int(input("Enter an integer value: "))
if(a==1):
    print("The day is Monday")
elif(a==2):
    print("The day is Tuesday")
elif(a==3):
    print("The day is Wednesday")
elif(a==4):
    print("The day is Thursday")
elif(a==5):
    print("The day is Friday")
elif(a==6):
    print("The day is Saturday")
elif(a==7):
    print("The day is Sunday")
else:
    print("Wrong input")
