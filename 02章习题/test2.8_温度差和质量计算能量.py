# 用户输入水的质量千克 水的初始稳定和最终温度 计算能量

initialTemplate = eval(input("请输入初始温度：") or "3.5")
finalTemplate = eval(input("请输入最终温度：") or "10.5")
kilograms = eval(input("请输入水的质量千克数：") or "55.5")

energy = kilograms * (finalTemplate - initialTemplate) * 4184

print("热量需要:", energy)
