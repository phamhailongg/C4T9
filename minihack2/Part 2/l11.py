# make a list 
n = input("Enter a list of numbers, separated by ‘, ‘ : ")
n = n.split(',')
print(n)
ln1 = []
for i in n : 
    i = int(i)
    ln1.append(i)
print("All even numbers from entered list: ")
for a in ln1 : 
    if a % 2 == 0 : 
        print(*ln1, sep=", ")