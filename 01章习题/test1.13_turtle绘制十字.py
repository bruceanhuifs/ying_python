# turtle绘制十字

import turtle
turtle.showturtle()
turtle.speed(1)

turtle.penup()
turtle.goto(0, 50)
turtle.pendown()

turtle.right(90)
turtle.forward(100)

turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.left(90)
turtle.forward(100)

turtle.done()