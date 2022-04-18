# 小计和酬金率求小费和总费用

subTotal, feeRate = eval(input("请输入小计和酬金率，以美式逗号分隔：") or "15.69, 15")
gratuity = int(subTotal * feeRate) / 100
totalFee = subTotal + gratuity

print("你需要支付的小费是", gratuity, "总费用是：", totalFee)

