# 显示时间 输入秒数计算多少分钟多少秒

seconds = eval(input("请输入多少秒“："))
minutes = seconds // 60
remainingSeconds = seconds % 60

print(seconds, "秒等于", minutes, "分钟", remainingSeconds, "秒钟")
