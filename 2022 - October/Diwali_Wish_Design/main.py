from turtle import *

setup(800, 600)
bgcolor("#FFFBC8")

pensize(1)
hideturtle()
penup()
speed(10)

goto(0, -250)

pendown()
color("#2E1503")
begin_fill()
circle(250)
end_fill()

penup()

pencolor("#FFFBC8")
goto(-95, 80)

write("H", font = ('Gabriola', 50, "normal"))
goto(-45, 80)
write("A", font = ('Gabriola', 50, "normal"))
goto(-5, 80)
write("P", font = ('Gabriola', 50, "normal"))
goto(35, 80)
write("P", font = ('Gabriola', 50, "normal"))
goto(75, 80)
write("Y", font = ('Gabriola', 50, "normal"))

goto(-120, -10)
write("D", font = ('Gabriola', 50, "normal"))
goto(-75, -10)
write("I", font = ('Gabriola', 50, "normal"))
goto(-50, -10)
write("W", font = ('Gabriola', 50, "normal"))
goto(10, -10)
write("A", font = ('Gabriola', 50, "normal"))
goto(60, -10)
write("L", font = ('Gabriola', 50, "normal"))
goto(110, -10)
write("I", font = ('Gabriola', 50, "normal"))

goto(0, -80)
pendown()

# diya

color("#CC9966")
begin_fill()

right(35)

# first line
circle(70, 80)
right(130)

# second line
circle(-95,186)
right(130)

# third line
circle(72,85)

end_fill()


#flame
color("orange")
begin_fill()
circle(50,90)
left(90)
circle(50,90)
end_fill()

done()
