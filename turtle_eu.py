import turtle

turtle.mode("logo")
turtle.bgcolor("#003297")
t = turtle.Turtle()
t.color("#fec900")

def drawStar(size):
    t.pendown()
    t.setheading(90)
    t.forward(size/4)
    t.begin_fill()
    for i in range(0, 5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.left(72)
    t.end_fill()
    t.setheading(270)
    t.forward(size/4)
    t.penup()

def drawEU(size, distance):
    t.showturtle()
    t.penup()
    for i in range(0, 12):
        t.setheading(i * 30)
        predrawHeading = t.heading()
        t.forward(distance)
        drawStar(size)
        t.setheading(180 + predrawHeading)
        t.forward(distance)
        t.right(180)
    t.hideturtle()
        
drawEU(30, 275)
    