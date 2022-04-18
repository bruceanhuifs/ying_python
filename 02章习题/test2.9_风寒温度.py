# 用户输入华氏温度和风速计算风寒温度

fahrenheit = eval(input("请输入从-58至41的华氏温度:") or "5.3")
windSpeed = eval(input("请输入大于2的风速：") or "6")
windChill = 35.74 + 0.6215 * fahrenheit - 35.75 * windSpeed ** 0.16 + 0.4275 * fahrenheit * windSpeed ** 0.16

print("风寒温度是：", windChill)


