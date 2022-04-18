# 计算圆柱体的体积

radius, height = eval(input("请输入圆柱体的半径和高，中间以英文的逗号分隔：") or "5.5, 12")
area = radius ** 2 * 3.14
volume = area * height
print("圆柱体的底面积为：", area)
print("圆柱体的体积为：", volume)

