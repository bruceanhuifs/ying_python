# 输入4位数字整数 打印每位上的数字 从个位开始

int4WeiShu = eval(input("请输入四位整数：") or "5213")
geWeiShu = int4WeiShu % 10

int3WeiShu = int4WeiShu // 10

shiWeiShu = int3WeiShu % 10
int2WeiShu = int3WeiShu // 10

baiWeiShu = int2WeiShu % 10

qianWeiShu = int2WeiShu // 10

print(geWeiShu)
print(shiWeiShu)
print(baiWeiShu)
print(qianWeiShu)

