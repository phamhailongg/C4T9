import math
a = float(input("Enter coefficient a "))
b = float(input("Enter coefficient b "))
c = float(input("Enter coefficient c "))
d = b*b - 4*a*c
if d>0:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print("Root are real and unequal ",r1, " and ",r2)
elif d==0:
    r1 = -b/(2*a)
    print("Root are real and same ", r1)
else:
    print("No real roots are there")

