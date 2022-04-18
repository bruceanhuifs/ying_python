# 人口预测 输入年数

years = eval(input("请输入年数：") or "5")
# NOWPPL = 3120324986

NOWPPL = 312032486
yearMinus = 365 * 24 * 3600 * years

allPeople = NOWPPL + yearMinus // 7 - yearMinus // 13 + yearMinus // 45

print(years, "年后，人口数是：", allPeople)



