# check position 
n = [1, 12, 34, 56, 87, 19, 20, 77]
c = int(input("Enter a number: "))
if c in n :
    for i in range(0, len(n)) : 
        if n[i] == c : 
            print("Found, position: ", i + 1) 
else :             
    print("Not found in our list")

