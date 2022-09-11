import turtle
colors = ["red","purple","blue","green", "orange","White"]
my_pen=turtle.Pen()
turtle.bgcolor("white")
for x in range(360):
    my_pen.pencolor(colors[x%6])
    my_pen.width(x/100+1)
    my_pen.forward(x)    my_pen.left(59)


