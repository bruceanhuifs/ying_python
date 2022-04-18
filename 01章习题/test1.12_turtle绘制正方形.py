# turtle 绘制正方形

import turtle
turtle.showturtle()
turtle.speed(1)

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)


turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.done()
