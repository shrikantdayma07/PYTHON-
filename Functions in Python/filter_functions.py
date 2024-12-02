#filter function : used to filter value from sequence based on condition 
#syntax : filter(function,sequence)

# def is_even(n):
#     if n % 2 == 0:
#         return True
#print(is_even(4))
# print(is_even(3))   #it will return none 

#using regular function
#l=[1,2,3,4,5,6,7,8,9,10]
# def is_even(n):
#     if n % 2 == 0:
#         return True 
    
# l1=list(filter(is_even,l))
# print(l1)

#using lambda function
l=[1,2,3,4,5,6,7,8,9,10]
l2=list(filter(lambda i : i%2==0,l))
print("l2=",l2)