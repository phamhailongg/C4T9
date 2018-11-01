# Ask user to enter a number n, then print n x n numbers, following multiplication table’s pattern

x = int(input("Number? "))

def print_multiples(n):
    for i in range(1, x + 1) :
        print(n * i, end="\t")
    print()

for i in range(1, x + 1) :
    print_multiples(i)



