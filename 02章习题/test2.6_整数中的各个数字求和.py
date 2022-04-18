# 整数中各个数字求和

intNumbers = eval(input("请输入1-999的任意：") or "999")
geWeiShu = intNumbers % 10
shengYuShuShiBaiWei = intNumbers // 10
shiWeiShu = shengYuShuShiBaiWei % 10
shengYuShuBaiWei = shengYuShuShiBaiWei // 10
baiWeiShu = shengYuShuBaiWei % 10

print(geWeiShu + shiWeiShu + baiWeiShu)
