# 绘制四个正六边形

import turtle

turtle.showturtle()
turtle.speed(1)

turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.color("red")
turtle.left(30)
turtle.forward(60)

turtle.left(60)
turtle.forward(60)

turtle.left(60)
turtle.forward(60)

turtle.left(60)
turtle.forward(60)

turtle.left(60)
turtle.forward(60)

turtle.left(60)
turtle.forward(60)

turtle.color("black")
turtle.forward(60)

turtle.right(60)
turtle.forward(60)

turtle.right(60)
turtle.forward(60)

turtle.right(60)
turtle.forward(60)

turtle.right(60)
turtle.forward(60)

turtle.right(60)
turtle.forward(60)


# 绘制左侧2个正六边形

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.color("blue")

turtle.forward(60)

turtle.left(60)
turtle.forward(60)

turtle.left(60)
turtle.forward(60)

turtle.left(60)
turtle.forward(60)

turtle.left(60)
turtle.forward(60)

turtle.left(60)
turtle.forward(60)

turtle.color("green")
turtle.forward(60)

turtle.right(60)
turtle.forward(60)

turtle.right(60)
turtle.forward(60)

turtle.right(60)
turtle.forward(60)

turtle.right(60)
turtle.forward(60)

turtle.right(60)
turtle.forward(60)

turtle.done()


