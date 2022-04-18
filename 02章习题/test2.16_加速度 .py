# 加速度
speed0, speed1, time = eval(input("请输入初始速度，最后速度，间隔时间：") or "5.5, 50.9, 4.5")

accelaration = (speed1 - speed0) / time

print("加速度是：", accelaration)
