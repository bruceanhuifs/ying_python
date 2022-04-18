# turtle绘制时钟
import turtle

turtle.showturtle()
turtle.speed(3)

turtle.circle(100)

turtle.write("6")
turtle.penup()
turtle.goto(90, 100)
turtle.pendown()
turtle.write("3")

turtle.penup()
turtle.goto(-5, 180)
turtle.pendown()
turtle.write("12")

turtle.penup()
turtle.goto(-95, 100)
turtle.pendown()
turtle.write("9")

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.goto(-40, 100)
turtle.goto(60, 100)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.goto(0, 180)

turtle.penup()
turtle.goto(-10, -20)
turtle.pendown()
turtle.write("9:15:00")

turtle.done()