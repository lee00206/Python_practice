import turtle

turtle.color("black")
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()

turtle.begin_fill()
turtle.color("yellow")
turtle.circle(200)
turtle.end_fill()

turtle.penup()
turtle.goto(-100,130)
turtle.pendown()

turtle.begin_fill()
turtle.color("black")
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(100,130)
turtle.pendown()

turtle.begin_fill()
turtle.color("black")
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(0,-70)
turtle.pensize(5)
turtle.pendown()

turtle.circle(120,90)

turtle.penup()
turtle.setheading(180)
turtle.goto(0,-70)
turtle.pendown()

turtle.circle(-120,90)

turtle.penup()
turtle.goto(-20,70)
turtle.setheading(360)
turtle.pendown()

turtle.begin_fill()
turtle.color("orange")
turtle.forward(40)
turtle.left(120)
turtle.forward(40)
turtle.left(120)
turtle.forward(40)
turtle.end_fill()

turtle.penup()
turtle.goto(-100, -80)
turtle.pendown()

turtle.begin_fill()
turtle.color("red")
turtle.goto(-100, -200)

turtle.penup()
turtle.goto(100, -80)
turtle.pendown()

turtle.goto(100, -200)
turtle.end_fill()

turtle.penup()
turtle.goto(-200, 80)
turtle.pendown()

turtle.begin_fill()
turtle.color("black")
turtle.goto(-300, -150)
turtle.goto(-100, -150)
turtle.goto(-200,80)

turtle.penup()
turtle.goto(200, 80)
turtle.pendown()

turtle.goto(300, -150)
turtle.goto(100, -150)
turtle.goto(200,80)
turtle.end_fill()
    
turtle.done()
