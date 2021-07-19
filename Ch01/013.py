# 013
import time

# time.time 取得當前秒數
# 從 1970/0/0 0:00 開始計算,直到目前的總計秒數
str = time.time()
print(str)

# 用 time.time 與之前的時間做比較
start = time.time()
end = time.time()-start
print(start)
print(end)

# time.localtime 取得當前時間 tuple
local = time.localtime()
# output: time.struct_time(tm_year=2021, tm_mon=7, tm_mday=19, tm_hour=21, tm_min=7, tm_sec=32, tm_wday=0, tm_yday=200, tm_isdst=0)
print(local)

print(local[0])
print(local[1])

# time.clock 取得當前時間秒數
# measure process time
# Error(???) -> AttributeError: module 'time' has no attribute 'clock'
# cltime = time.clock()
# print(cltime)

# time.ctime 秒數轉換成字串
ct = time.ctime()
print(ct)

ct = time.time()
print(time.ctime(ct))

# time.mktime 時間 tuple 轉換成秒數
t = (2017, 2, 17, 17, 3, 38, 1, 48, 0)
ti = time.mktime(t)
print(ti)
print(time.mktime(time.localtime()))

# time.gmtime 秒數轉換成時間 tuple
gt = time.gmtime(time.time())
print(gt)
t = (2017, 2, 17, 17, 3, 38, 1, 48, 0)
t1 = time.mktime(t)
t2 = time.gmtime(time.mktime(t))
print(t1)
print(t2)

# time.strftime 時間 tuple 轉換成特定格是字串
t0 = (2017, 2, 17, 17, 3, 38, 1, 48, 0)
t0 = time.mktime(t0)
print(time.strftime("%b-%d-%Y %H:%M:%S", time.gmtime(t0)))

# time.strptime 轉換字串至時間物件
t2 = time.strptime("12:30:25", "%H:%M:%S")
print(t2)

# time.sleep 秒數延遲
t = time.time()
print(t)
time.sleep(3)
t = time.time()
print(t)
