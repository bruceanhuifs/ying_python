# 绘制四个圆

'''speed – 一个 0…10 范围内的整型数或速度字符串 (见下)
设置海龟移动的速度为 0…10 表示的整型数值。如未指定参数则返回当前速度。
如果输入数值大于 10 或小于 0.5 则速度设为 0。速度字符串与速度值的对应关系如下:
“fastest”: 0 最快
“fast”: 10 快
“normal”: 6 正常
“slow”: 3 慢
“slowest”: 1 最慢
速度值从 1 到 10，画线和海龟转向的动画效果逐级加快。
'''

import turtle

radius = eval(input("请输入圆的半径："))
turtle.showturtle()
turtle.speed(1)

turtle.penup()
turtle.goto(radius, radius)
turtle.pendown()
turtle.color("red")
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, -radius)
turtle.pendown()
turtle.color("black")
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius, -radius)
turtle.pendown()
turtle.color("blue")
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius, radius)
turtle.pendown()
turtle.color("green")
turtle.circle(radius)

turtle.done()


