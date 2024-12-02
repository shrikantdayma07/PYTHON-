#write a program to remove duplicates from the string 
# s="abcab"
# s1=" "
# for i in s:
#     if i not in s1:
#         s1+=i
# print(s1)

# s="tsutsugamushi"
# s1=" "
# for i in s:
#     if i not in s1:
#         s1+=i
# print(s1)


#WAP to find no of occurrencess of each character present in the given string
# Accept a string from the user
input_string = input("Enter a string: ")

# Keep track of characters we already counted
counted_chars = ""

# Print the counts
print("Character counts:")
for char in input_string:
    if char not in counted_chars:  # Check if the character is already counted
        # Count the occurrences of the character
        count = 0
        for c in input_string:
            if c == char:
                count += 1
        print(f"{char}: {count}")
        # Add the character to counted_chars so it's not counted again
        counted_chars += char
