# Viết chương trình dùng turtle vẽ một hình đa giác, đa giác này có số cạnh do người dùng nhập vào
n = int(input("Number of edges: "))

from turtle import * 

for i in range(n): 
    fd(100)
    lt(360 / n)

mainloop()