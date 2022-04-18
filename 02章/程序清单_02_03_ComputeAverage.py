# 计算三个数的平均值
print("Enter three numbers: ")
number1 = eval(input())
number2 = eval(input())
number3 = eval(input())

print(number1)
# Compute average
average = (number1 + number2 + number3) / 3

# Display result
print(average)



number1, number2, number3 = eval(input("请输入三个数字，分别用英文输入法的逗号分隔:") or "1, 2, 3")
average = int((number1 + number2 + number3) / 3)
print("这三个数的均值是：", average)
