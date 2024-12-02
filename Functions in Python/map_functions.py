#map function : it is used when we want to apply some functionality on entire sequence 
#if i have the list and i want the square of that particular list then i go for map function

#using regular function
# l=[1,2,3,4,5,6,7,8,9,10]
# def square1(n):
#     return n*n
# square_of_l = list(map(square1,l))
# print(square_of_l)

#using lambda function 
l=[1,2,3,4,5,6,7,8,9,10]
square_of_l = list(map(lambda n : n*n, l))
print(square_of_l)