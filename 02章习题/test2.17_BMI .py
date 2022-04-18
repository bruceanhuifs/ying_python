# BMI
height, weight = eval(input("请输入身高英尺，重量磅：") or "5, 95.5")

BMI = weight * 0.45359237 / ((height * 0.0254) ** 2) / 100


print("BMI是：", BMI)
