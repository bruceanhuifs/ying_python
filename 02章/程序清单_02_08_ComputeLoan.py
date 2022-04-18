# 计算贷款总数 和 月供数

years = eval(input("请输入贷款的年数：") or "15")
loan = eval(input("请输入贷款的数量：") or "250000")
yearRate = eval(input("请输入贷款的年利率：") or "5.75")
monthRate = yearRate / 1200

monthLoan = loan * monthRate / (1 - 1 / (1 + monthRate) ** (years * 12))
allLoan = monthLoan * 12 * years

print(allLoan)
print(monthLoan)

print("保留小数点后2位的总还款数量是：", int(allLoan * 100) / 100)
print("保留小数点后2位的月供数量是：", int(monthLoan * 100) / 100)
