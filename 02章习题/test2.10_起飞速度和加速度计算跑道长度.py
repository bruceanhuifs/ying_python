# 飞机起飞速度和加速度计算跑道长度

speedZero = eval(input("请输入起飞速度 ：") or "60")
jiaSpeed = eval(input("请输入加速度：") or "3.5")

length = speedZero * speedZero / (2 * jiaSpeed)

print("这个飞机最小的跑道长度是：", length, "米")



