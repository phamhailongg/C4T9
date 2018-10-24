# Sử dụng turtle vẽ 3 hình vuông, mỗi hình vuông cách nhau 30 độ như hình
from turtle import * 

for i in range(4):
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)

    lt(-30)

mainloop()