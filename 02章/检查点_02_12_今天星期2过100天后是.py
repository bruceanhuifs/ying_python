# 今天星期2过100天后是

today = eval(input("请输入今天是星期几：") or "2")
howDay = eval(input("请输入过了多少天：") or "100")
nowDay = (today + howDay) % 7
print("今天是星期", today, "过了", howDay, "天后是",
      "星期", nowDay)



