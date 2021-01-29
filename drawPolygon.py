import turtle

def drawPolygon(x = 0, y = 0, radius = 50, numberOfSides = 3):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    newy = y + 2*radius
    newx = x - radius
    turtle.goto(newx, newy)
    turtle.pendown()
    for i in range(0, numberOfSides):
        turtle.forward(radius*2)
        turtle.right(360/numberOfSides)

