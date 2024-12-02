#as soon as the number is even it will skip the number and print the next number i.e. odd numbers only /-
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)