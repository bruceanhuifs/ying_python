# turtle绘制直线

import turtle

x1 = eval(input("请输入x1坐标："))
y1 = eval(input("请输入y1坐标："))

x2 = eval(input("请输入x2坐标："))
y2 = eval(input("请输入y2坐标："))

turtle.showturtle()
turtle.speed(1)

turtle.penup()
turtle.goto(x1, y1)
turtle.write(f"起点的坐标是：{x1},{y1}")
turtle.pendown()

turtle.goto(x2, y2)
turtle.write(f"终点的坐标是：{x2},{y2}")

turtle.done()

