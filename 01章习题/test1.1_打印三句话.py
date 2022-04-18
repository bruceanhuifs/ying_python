# 打印三句话(纵向)?
print("欢迎学习Python")
print("欢迎学习计算机科学")
print("程序是有趣的")

# 自己加换行符
print("欢迎学习Python\n欢迎学习计算机科学\n程序是有趣的")

print("欢迎学习Python\n"
      "欢迎学习计算机科学\n"
      "程序是有趣的")

print("欢迎学习Python\n" +
      "欢迎学习计算机科学\n" +
      "程序是有趣的")

# 加了，逗号 就不对齐了
print("欢迎学习Python\n",
      "欢迎学习计算机科学\n",
      "程序是有趣的\n")

# 打印三句话(横向)? 每句后面用空格或者其他符号分开（如逗号）
# 参考： https://www.runoob.com/w3cnote/python3-print-func-b.html
print("欢迎学习Python", "欢迎学习计算机科学", "程序是有趣的")

print("欢迎学习Python,", "欢迎学习计算机科学,", "程序是有趣的")

print("欢迎学习Python", end="，")
print("欢迎学习计算机科学", end="，")
print("程序是有趣的", end="，")

# 自己加多段的分割符号格式化三句话
print("欢迎学习Python\
      欢迎学习计算机科学\
      程序是有趣的")