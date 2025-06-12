import turtle
my_pen=turtle.Turtle()
turtle.bgcolor("black")
colors=["red","purple","blue","green","orange","yellow"]
for x in range(360):
    my_pen.pencolor(colors[x%6])
    my_pen.width(x/100+1)
    my_pen.forward(x)
    my_pen.left(59)
turtle.done()
                
