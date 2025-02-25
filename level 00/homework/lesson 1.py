from turtle import * 

#we want to paint a house

#step 1: draw a square
width(7)
begin_fill()
color("grey")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square
forward(70)
#(drawing a door)

left(90)
begin_fill()
color("brown")

forward(70) #height of the door
right(90)
forward(50)
right(90)
forward(70)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(139)
forward(150)

left(97)
forward(152)
end_fill()

penup()
goto(20, 130)
pendown()

left(200)

right(67.5)
begin_fill()
color("blue")

forward(50)
left(90)

forward(40)
left(90)

forward(50)
left(90)

forward(40)
end_fill()

penup()
goto(130, 170)
pendown()

begin_fill()
left(90)
forward(50)
right(90)

forward(40)
right(90)

forward(50)
right(90)

forward(40)
end_fill()
exitonclick()
