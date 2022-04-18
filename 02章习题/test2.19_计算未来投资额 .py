# 计算未来投资额

investment = eval(input("请输入投资金额：") or "1000")
annualRate = eval(input("请输入年利率：") or "4.25")
years = eval(input("请输入投资的年数：") or "1")

investmentAccumulate = investment * (1 + annualRate / 1200) ** (years * 12)

print("你未来的投资额是：", investmentAccumulate)