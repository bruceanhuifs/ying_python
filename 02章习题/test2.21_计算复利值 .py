# 计算复利值

monthDeposit = eval(input("输入每个月存的值：") or "100")
annualRate = eval(input("输入年利率：") or "5")
months = eval(input("输入几个月：") or "6")

# value = monthDeposit * ((1 + annualRate / 1200) + (1 + annualRate / 1200) ** 2 + (1 + annualRate / 1200) ** 3 +
#                         (1 + annualRate / 1200) ** 4 + (1 + annualRate / 1200) ** 5 +
#                         (1 + annualRate / 1200) ** 6)
value = 0
i = 1
while i < (months + 1):
    value += monthDeposit * (1 + annualRate / 1200) ** i
    i += 1

print(months, "个月后你可以得到：", value)


