# 人口预测
years = eval(input("请输入年数："))
nowPeople = 3120324986
oneYearMinus = 365 * 24 * 3600

allPeople = nowPeople + (oneYearMinus//7 - oneYearMinus//13 + oneYearMinus//45) * years

print(f"这是第{years}年的总人口数量：{allPeople}")



