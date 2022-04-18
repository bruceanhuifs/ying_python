# turtle绘制立方体
import turtle

turtle.showturtle()
turtle.speed(1)

turtle.goto(200, 0)
turtle.goto(200, 100)
turtle.goto(0, 100)
turtle.goto(0, 0)

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()

turtle.goto(100, -50)
turtle.goto(100, 50)
turtle.goto(-100, 50)
turtle.goto(-100, -50)

turtle.goto(0, 0)
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.goto(200, 0)

turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.goto(200, 100)

turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.goto(0, 100)

turtle.done()


