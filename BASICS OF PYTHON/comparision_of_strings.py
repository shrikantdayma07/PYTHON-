#print('A' > 'a')

#find function
# a='Python Programming'
# print(a.find("P"))
# print(a.find("n"))

#index function
# a='Python Programming'
# print(a.index("c")) #o/p : ValueError

#count function
# a="Python Programming"
# print(a.count("P"))

#wap to print no. of occurances without using the count function
s=input("Enter your string : ")
substring = input("Enter your substring : ")
c=0
for i in s:
    if i==substring:
        c+=1
print("No. of occurances ",substring," is ", c)