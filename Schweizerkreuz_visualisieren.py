from turtle import *

Screen().setup(800,800)
Screen().bgcolor("red")

hideturtle()

pensize(5)
pencolor('white')
fillcolor('white')

s = 200

penup()
goto( -100, +200)
color("white")
fillcolor("white")

pendown()
begin_fill()
forward(s) # 100 Pixel
right(90)
forward(s) # 100 Pixel
left(90)
forward(s) # 100 Pixel
right(90)
forward(s) # 100 Pixel
right(90)
forward(s) # 100 Pixel
left(90)
forward(s) # 100 Pixel
right(90)
forward(s) # 100 Pixel
right(90)
forward(s) # 100 Pixel
left(90)
forward(s) # 100 Pixel
right(90)
forward(s) # 100 Pixel
right(90)
forward(s) # 100 Pixel
left(90)
forward(s) # 100 Pixel
end_fill()

done() # hält das Fenster offen
#change für Github