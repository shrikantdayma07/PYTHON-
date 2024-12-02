# accessing elements of a sequence using [] (indexing operator)

# syntax : [start : end : step]

#credit_number = "1234-5678-91011"
# #print(credit_number[0]) //output will be 1 as indexing start from 0

# #print(credit_number[2])

# #print(credit_number[0:4]) --->>gives output as 1234

credit_number = "1234-5678-91011"
print(credit_number[:3]) 
#as i have not mentioned the starting indexing so it assumed it as 0

# #print(credit_number[5:]) if you want the numbers starting from 5 and upto the end then no need to mention the ending index 

# #print(credit_number[-1]) this will print the last number inside the variable 

# #print(credit_number[-2]) #last 2nd digit 

# #print(credit_number[::2]) #this will print every second number starting from the beginning till end 

# #print(credit_number[::3])  #this will print every third number from the starting till end !!

# '''last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX - {last_digits}")'''

# credit_number = credit_number[::-1]
# print(credit_number) #this print the credit number in the reverse order 

# name="Shrikant"
# #print(name[0:5])
# #print(name[0:])
# #print(name[:9])
# #print(name[::2])
# print(name[-1])