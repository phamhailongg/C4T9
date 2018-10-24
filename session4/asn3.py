# Sử dụng turtle vẽ 30 hình vuông, các hình vuông không chồng lên nhau như hình
from turtle import *
shape("turtle")

for i in range(30):
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)

    lt(1)

mainloop()
