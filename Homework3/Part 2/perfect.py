# test perfect number

n = int(input("Enter the number: "))
result = 0

for i in range(1, n) :
    if (n % i) == 0:
        result = result + i
if result == n :
    print(n, "is a perfect number!") 
else : 
    print(n, "is NOT a perfect number!")
        

