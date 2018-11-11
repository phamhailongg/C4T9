# make a list 
n = input("Enter a list of numbers, separated by ‘ ‘ : ")
n = n.split(' ')
ln = []
for i in n : 
    i = int(i)
    ln.append(i)
print("Sum of all entered numbers: ", sum(ln))


