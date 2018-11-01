# 9 x 9 numbers (multiplication table)

def print_multiples(n):
    for i in range(1, 10):
        print(n * i, end=" ")
    print()

for i in range(1, 10):
    print_multiples(i)