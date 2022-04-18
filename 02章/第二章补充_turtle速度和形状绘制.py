# import package  用不同的形状绘制 默认是三角形
import turtle
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

turtle.speed(3)

# for default shape
turtle.forward(100)

# for circle shape
turtle.shape("circle")
turtle.right(60)
turtle.forward(100)

# for triangle shape
turtle.shape("triangle")
turtle.right(60)
turtle.forward(100)

# for square shape
turtle.shape("square")
turtle.right(60)
turtle.forward(100)

# for arrow shape
turtle.shape("arrow")
turtle.right(60)
turtle.forward(100)

# for turtle shape
turtle.shape("turtle")
turtle.right(60)
turtle.forward(100)
turtle.done()