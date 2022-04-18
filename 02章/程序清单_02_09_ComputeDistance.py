# 计算2点距离

# 方法一
x1 = eval(input("请输入第一个点的坐标x1：") or "1.5")
y1 = eval(input("请输入第一个点的坐标y1：") or "-3.4")

x2 = eval(input("请输入第二个点的坐标x2：") or "4")
y2 = eval(input("请输入第二个点的坐标y2：") or "5")

# 方法二
# x1, y1 = eval(input("请输入第一个点的坐标，2个数用英文输入逗号隔开：") or "1.5, -3.4")
# x2, y2 = eval(input("请输入第一个点的坐标，2个数用英文输入逗号隔开：") or "4, 5")

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)
