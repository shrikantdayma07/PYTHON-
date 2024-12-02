# Dictionary : it is a group or collection of key-value pairs enclosed in curly braces 

# syntax : {key:value, key:value, key:value, key:value, ..... }

# d={1:1,2:4,3:9,4:16,5:25}
# print(d)
# print(len(d))

# dict = {"Name":"Shrikant", "subject":"Python", "roll no." : 74}
# print(dict)
# print(len(dict))

# in dictionary, duplicates values are not allowed ... values can be duplicate but key should be unique !!
# indexing and slicing is not allowed in dictionary !!

# Accessing values using key name 
# syntax : dict[key]

# dict1 = {"Name":"Shrikant", "subject":"Python", "roll no." : 74}
# print(dict1["Name"])
# print(dict1["roll no."])

# to update or to add any key/value in a dictionary 
# dict1 = {"Name":"Shrikant", "subject":"Python", "roll no." : 74}
# dict1["Name"]="Anuj"  #O/P : {'Name': 'Anuj', 'subject': 'Python', 'roll no.': 74}
# dict1["subject"]="Java" #O/P : {'Name': 'Anuj', 'subject': 'Java', 'roll no.': 74}
# print(dict1)  

# del() keyword 
# dict={'Name': 'Anuj', 'subject': 'Java', 'roll no.': 74}
# del dict["subject"]
# print(dict)

# clear() keyword : it will clear only not data not entire dictionary (from memory)
# d={1:1,2:4,3:9,4:16,5:25}
# d.clear()
# print(d)

# del () : it will delete entire dictionary from the memory 
# d={1:1,2:4,3:9,4:16,5:25}

# del d


# dict () - creates a dictionary 
# d=dict()
# print(type(d))

# input from the user 
# dic = eval(input("Enter dictionary : "))
# print(type(dic))

# get() fucntion : to get value associated with the key 
# dict1={"Name":"Shrikant","Age":21,"subject":"Maths"}
# get()

# print(dict1.get("Name")) #it will return the name present in the dictionary 
# if key is not available then it will retutn 'None'

#pop() : it removes the entry associated with the specified key and return the corresponding value 
#if key is not present then it will give 'KeyError'
# dict1={"Name":"Shrikant","Age":21,"subject":"Maths"}
# print(dict1.pop("Name"))
# print(dict1) #it will remove name from the dictionary we defined ... and also will show what it has removed 

# keys() : it return list of keys 
# dict1={"Name":"Shrikant","Age":21,"subject":"Maths"}
# print(dict1.keys())

# values() : it will return list of all values present in the dictionary 
# dict1={"Name":"Shrikant","Age":21,"subject":"Maths","Bloodgp":"B+"}
# print(dict1.values())

# item() : it will return the pair of key and value in the braces inside the square bracket 
# dict1={"Name":"Shrikant","Age":21,"subject":"Maths"}
# print(dict1.items()) #([('Name', 'Shrikant'), ('Age', 21), ('subject', 'Maths')])

# popitem() : it removes an arbitrary(random) item(key-value) from the dictionary and return it.
# dict1={"Name":"Shrikant","Age":21,"subject":"Maths"}
# print(dict1.popitem())
# print(dict1) #it will delete random elements from the dictionary  #o/p : {'Name': 'Shrikant', 'Age': 21} -->> ('subject', 'Maths') is removed from the dictionary 


# copy() : it copies the previous dictionary
# dict1={"Name":"Shrikant","Age":21,"subject":"Maths"}
# d=dict1.copy()
# print(d)

# update() : d.update(x)
# x={"year":2024}
# d.update(x)
# print(d)

# dict comprehension : {exp:value for i in iterable_object}
# y={i:i**2 for i in range(1,11)}
# print(y) #o/p: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# z={"sql":80,"Web":80,"Python":50}
# s=0
# for i in z.values():
#     s+=i
# print(s) #o/p: 210

#this is the code when i have only one string 
# z={"Name":"Shrikant","sql":80,"Web":80,"Python":50}
# s=0
# for i in z.values():
#     if i == "Shrikant":
#         continue
#     s+=i
# print(s) #o/p: 210

#when i have multiple strings 
z={"name":"shrikant","age":21,"subject":"Maths","Roll No.":74,"Marks":80}
s=0
for i in z.values():
    if isinstance(i,int):
        s+=i 
print(s)