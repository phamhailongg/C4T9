# turtle
from turtle import * 
import random 
bgcolor("black")
c = ["red", "blue", "yellow", "green", "pink", "Orange"]
speed(5)
for j in range(3, 10):
    for i in range(j):
        color(random.sample(c, 1))
        fd(100)
        lt(360/j)



mainloop()