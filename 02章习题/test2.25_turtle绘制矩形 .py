# 绘制矩形 输入矩形的中心 长 宽

import turtle

x = eval(input("请输入矩形的中心x："))
y = eval(input("请输入矩形的中心y："))
long = eval(input("请输入矩形的长："))
height = eval(input("请输入矩形的宽："))

x1 = x - long / 2
y1 = y - height / 2

turtle.showturtle()
turtle.speed(1)

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()

turtle.forward(long)
turtle.left(90)
turtle.forward(height)

turtle.left(90)
turtle.forward(long)

turtle.left(90)
turtle.forward(height)

turtle.done()


