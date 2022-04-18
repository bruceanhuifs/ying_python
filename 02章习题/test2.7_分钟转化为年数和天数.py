# 分钟转化为年数和天数

allMinutes = eval(input("请输入多少分钟数：") or "1000000000" )
allDays = allMinutes // 1440
minutes = allMinutes % 1440

allYears = allDays // 365
days = allDays % 365

print(allMinutes, "近似等于", allYears, "年", days, "天")
