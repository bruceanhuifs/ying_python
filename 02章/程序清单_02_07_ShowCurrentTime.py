# 当前时间是多少小时 分钟 秒钟
# 北京时间=GMT时间+8小时。GMT:格林尼治Greenwich Mean Time标准时间。

import time
currentTime = time.time()
totalSeconds = int(currentTime)

currentSeconds = totalSeconds % 60
totalMinutes = totalSeconds // 60

currentMinutes = totalMinutes % 60
totalHours = totalMinutes // 60

currentHours = totalHours % 24


print(f"现在格林尼时间是：{currentHours}:{currentMinutes}:{currentSeconds} GMT, 北京时间为：\
{currentHours+8}:{currentMinutes}:{currentSeconds}")
