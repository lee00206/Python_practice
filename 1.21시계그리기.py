import turtle

turtle.color("black")
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()

turtle.circle(100)

turtle.penup()
turtle.goto(0,80)
turtle.write("12",font=("Arial", 15, "normal"))
turtle.pendown()

turtle.penup()
turtle.goto(80,0)
turtle.write("3",font=("Arial", 15, "normal"))
turtle.pendown()

turtle.penup()
turtle.goto(0,-90)
turtle.write("6",font=("Arial", 15, "normal"))
turtle.pendown()

turtle.penup()
turtle.goto(-20,-120)
turtle.write("9:15:00",font=("Arial", 15, "normal"))
turtle.pendown()

turtle.penup()
turtle.goto(-80,0)
turtle.write("9", font=("Arial", 15, "normal"))
turtle.pendown()

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.goto(0,70)

turtle.penup()
turtle.goto(-60,0)
turtle.pendown()

turtle.goto(60,0)

turtle.done()
