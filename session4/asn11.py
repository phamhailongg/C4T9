# draw and fill yellow color to a triangle

from turtle import *

color("green", "yellow")
begin_fill()

for i in range(3):
    fd(200)
    lt(120)

end_fill()

mainloop()