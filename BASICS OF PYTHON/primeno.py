#this code will print the prime number 
num = int(input("Enter an integer number : "))
for i in range(2,num):
    if num % i == 0:
        print('not prime')
        break
else:
    print('prime')

