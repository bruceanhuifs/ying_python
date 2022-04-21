# 用户输入一个 数字计算能换算出 除美元外 25美分 10美分 5美分 1美分 最少的硬币数量

amount = eval(input("请输入多少美元（例如11.56美元）：") or "11.56")

remainingAmount = int(amount * 100)

dollars = remainingAmount // 100
remainingAmount %= 100

cents25 = remainingAmount // 25
remainingAmount %= 25

cents10 = remainingAmount // 10
remainingAmount %= 10

cents5 = remainingAmount // 5

remainingAmount %= 5

cents1 = remainingAmount

print("\t", "你输入了", amount, "美元\n",
      # "\t", dollars, "美元\n",
      "\t", "可以换算出最少的硬币数量是：\n",
      "\t", cents25, "个,", "25美分\n",
      "\t", cents10, "个,", "10美分\n",
      "\t", cents5, "个,", "5美分\n",
      "\t", cents1, "个,", "1美分\n" )


