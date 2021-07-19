# 012
import time
# 1970/1/1 0:00 至當前的秒數
ticks = time.time()
print(ticks)

#
ticks = time.ctime()
print(ticks)

# TimeTuple 時間格式操作
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print(t)
gt = time.gmtime(t)
print(gt)

# 字串轉時間(str), 透過 strptime 轉出來的格是為 TimeTuple
strtime = time.strptime("09:30:20", "%H:%M:%S")
print(strtime)

strtime = time.strptime("2017/09/30 09:30:20", "%Y/%m/%d %H:%M:%S")
print(strtime)

# 轉換秒數
strtime = time.mktime(time.strptime(
    "2017/09/30 09:30:20", "%Y/%m/%d %H:%M:%S"))
print(strtime)

# 若沒有指定日期到 timetuple, 則無法轉換成 tick 時間格式
# strtime = time.mktime(time.strptime("09:30:20", "%H:%M:%S"))
# print(strtime)
