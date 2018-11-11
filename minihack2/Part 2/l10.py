# even or odd 
n = [1, 12, 34, 56, 87, 19, 20, 77]
l = [] 
for i in n : 
    if  i % 2 == 0 : 
        l.append(i)
print("Sum of all entered numbers: ")
print(*l, sep=", ")
            