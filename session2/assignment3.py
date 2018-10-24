# draw triangle with turtle
from turtle import *
color("red")
begin_fill()
for i in range(3):
    forward(100)
    left(120)
end_fill()
mainloop()