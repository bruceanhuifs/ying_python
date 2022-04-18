# turtle绘制四个圆

import turtle
turtle.showturtle()
turtle.speed(1)

turtle.color("red")
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.circle(100)

turtle.color("blue")
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.circle(100)

turtle.color("black")
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.circle(100)

turtle.color("green")
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.circle(100)

turtle.done()
