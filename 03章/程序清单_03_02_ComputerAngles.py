# 计算角度

import math

x1, y1, x2, y2, x3, y3, = eval(input("请输入三角形的三个点的坐标,每个数字用英文的逗号隔开(例如 x1,y1,x2,y2,x3,y3):") or "1,1,6.5,1,6.5,2.5")

aBian = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
bBian = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
cBian = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

agreeA = math.degrees(math.acos((aBian ** 2 - bBian ** 2 - cBian ** 2) / (-2 * bBian * cBian)))
agreeB = math.degrees(math.acos((bBian ** 2 - aBian ** 2 - cBian ** 2) / (-2 * aBian * cBian)))
agreeC = math.degrees(math.acos((cBian ** 2 - aBian ** 2 - bBian ** 2) / (-2 * aBian * bBian)))

print("A角度为：", round(agreeA, 2), "B角度为：", round(agreeB, 2), "C角度为：", round(agreeC, 2))
