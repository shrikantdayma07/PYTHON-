#this program helps us to understand the concept of the recursive function 
# def factorial(n):
#     if n == 0:
#         result = 1
#     else:
#         result = n * factorial(n-1)
#     return result

# print("Factorial of 4 is:", factorial(4))

#using def keyword -->>functions 
# def square_number(n):
#     return n ** 2
# print("the square of 3 is: ",square_number(3))

#without using the def keyword 
# square = lambda n : n * n
# print("The square of 5 is : ",square(5))

#code to print the addition of two numbers using the def keyword 
# def addition(x,y):
#     return x + y 
# print("The sum of 4,5 is: ",addition(4,5))

#to perform addition of two numbers without using the def keyword --->> lambda keyword 
# sum1 = lambda x,y : x+y
# print(sum1(5,6))

#code to print greater of 3 numbers 
# def greater(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b 
#     else:
#         return c 
# print("The greater number is: ",greater(4,5,2))

greater = lambda x,y,z :x if x>y and x>z else y if y>z else z
print(greater(60,45,5))