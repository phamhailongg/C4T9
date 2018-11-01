# Ask users to enter a number, then print n positive numbers from 0 to n-1

x = int(input("Enter a number? "))

for i in range(0, x):
    print(i, end=" ")