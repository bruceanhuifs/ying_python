# 求销售税保留小数点后2位

salesMoney = eval(input("请输入多少钱："))
TAX = 0.06
salesTax = salesMoney * TAX
salesTax2Point = int(salesTax * 100) / 100

print(f"您购买需要付款{salesMoney}元钱，销售税率为{TAX},您需要\
支付的税是{salesTax}元，税钱保留到小数点后2位最终需支付的税款是{salesTax2Point}元")
