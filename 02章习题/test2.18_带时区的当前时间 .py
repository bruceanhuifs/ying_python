# 带时区的当前时间
import time

timeZone = eval(input("请输入时区：") or "-5")
allSeconds = int(time.time())

seconds = allSeconds % 60
allMinutes = allSeconds // 60
minutes = allMinutes % 60

allHours = allMinutes // 60

hours = allHours % 24

print("当前时间是：", hours + timeZone, ":", minutes, ":", seconds)

