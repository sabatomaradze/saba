from turtle import *


#we want to paint a house

#step 1: draw a square
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of scquare

#drawing a door


forward(70)
color("yellow")
left(90)
forward(120)           #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawing window

penup()
goto(180,180)

color("blue")
pendown()
begin_fill()
right(180)
right(60)
right(180)
forward(70)
left(90)
forward(45)
left(90)
forward(70)
left(90)
forward(45)
end_fill()

penup()
goto(20,180)

pendown()
begin_fill()
right(90)
forward(70)
right(90)
forward(45)
right(90)
forward(70)
right(90)
forward(45)
end_fill()




















exitonclick()