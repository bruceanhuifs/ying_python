# eval int round 区别

value = 4.6
print(int(value))  # 4
print(round(value))  # 5
print(eval("4 * 5 + 2"))  # 22
print(int("04"))  # 4
print(int("4.5"))  # error
print(eval("04"))  # error
