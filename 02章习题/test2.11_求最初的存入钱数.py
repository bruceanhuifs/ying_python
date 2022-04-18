# 用户输入目标的钱数，年数，年利率 求最初需要存多少钱

finalCount = eval(input("请输入最终想要获得钱数：") or "1000")
annualRate = eval(input("请输入年利率：") or "4.25")
years = eval(input("请输入存入的年数：") or "5")

initialCount = finalCount / ((1 + annualRate / 1200) ** (years * 12))

print("你最初需要存钱数为：", initialCount)
