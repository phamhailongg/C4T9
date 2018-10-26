# draw house
from turtle import *  
from math import *
speed(10)
penup() # turtle disappear
rt(90)
fd(300)
lt(90)
pendown() # turtle appear

# draw the house
for i in range(4):
    fd(400)
    lt(90)
fd(50)

# Draw door
color("blue")
begin_fill()
lt(90)
fd(220)
rt(90)
fd(90)
rt(90)
fd(220)
rt(90)
fd(90)
end_fill()

# draw window
penup()
rt(90)
fd(270)
rt(90)
fd(220)
pendown()
color("yellow")
begin_fill()
for i in range(4):
    fd(90)
    lt(90)
end_fill()

# Draw roof
penup()
lt(90)
fd(130)
rt(90)
fd(130)
lt(135)
pendown()
color("red")
begin_fill()
fd(200 * sqrt(2))
lt(90)
fd(200 * sqrt(2))
rt(45)
end_fill()


mainloop()
