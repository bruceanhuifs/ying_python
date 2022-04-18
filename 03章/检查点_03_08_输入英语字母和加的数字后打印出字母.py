# 输入一个字母和加几个数字后得到的字母

x = input("请输入一个英文字母：") or "A"
n = eval(input("请输入一个整数数字：") or "3")
zimu = chr(ord(x) + n)
print(zimu)




