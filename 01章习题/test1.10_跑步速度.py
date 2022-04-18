# 跑步速度
hours = eval(input("请输入小时数："))
minus = eval(input("请输入分钟数："))
seconds = eval(input("请输入秒钟数："))
gongLi = eval(input("请输入公里数："))

times = hours + minus/60 + seconds/3600

miles = gongLi/1.6

speed = miles/times
print(f"每小时的平均速度是：{speed} 英里/小时")

