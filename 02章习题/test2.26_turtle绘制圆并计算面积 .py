# 绘制圆 输入的圆心 半径 显示面积

import turtle

x = eval(input("请输入圆的中心x："))
y = eval(input("请输入圆的中心y："))
radius = eval(input("请输入圆的半径："))

area = radius ** 2 * 3.1415926

turtle.showturtle()
turtle.speed(1)

turtle.penup()
turtle.goto(x, y-radius)
turtle.pendown()

turtle.circle(radius)

turtle.penup()
turtle.goto(x, y)
turtle.write(area)

turtle.done()


