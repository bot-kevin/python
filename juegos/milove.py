import turtle
azadine = turtle.Turtle()

badis = turtle.Screen()
badis.bgcolor("black")
badis.title("I love you")

azadine.speed(1)
azadine.goto(0,-100)
azadine.pensize(9)

azadine.color("red")

azadine.begin_fill()
azadine.fillcolor("red")
azadine.left(140)
azadine.forward(180)
azadine.circle(-90,200)

azadine.setheading(60)
azadine.circle(-90,200)
azadine.forward(176)
azadine.end_fill()

azadine.setheading(140)
azadine.forward(170)
azadine.setheading(210)
azadine.forward(200)
azadine.setheading(-210)
azadine.setheading(390)
azadine.forward(600)

turtle.done()


