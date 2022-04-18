# turtle绘制多边形
# 输入值不输入就用默认值
# 参考： https://zhidao.baidu.com/question/503124176.html
import turtle

x1, y1 = eval(input("请输入x1,y1的坐标（两个数字间用逗号分隔）：") or "40, -69.28")  # 40, -69.28
x2, y2 = eval(input("请输入x2,y2的坐标（两个数字间用逗号分隔）：") or "-40, -69.28")  # -40, -69.28
x3, y3 = eval(input("请输入x3,y3的坐标（两个数字间用逗号分隔）：") or "-80, -9.8")  # -80, -9.8
x4, y4 = eval(input("请输入x4,y4的坐标（两个数字间用逗号分隔）：") or "-40, 69")  # -40, 69
x5, y5 = eval(input("请输入x5,y5的坐标（两个数字间用逗号分隔）：") or "40, 69")  # 40, 69
x6, y6 = eval(input("请输入x6,y6的坐标（两个数字间用逗号分隔）：") or "80, 0")  # 80, 0

turtle.showturtle()
turtle.speed(1)

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()

turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x4, y4)
turtle.goto(x5, y5)
turtle.goto(x6, y6)
turtle.goto(x1, y1)

turtle.done()
