# 014
import datetime

# time 套件不支援到微秒單位, 只 support 到秒
t1 = datetime.datetime.strptime("12:30:30.431234", "%H:%M:%S.%f")
print(t1)

# 可以進行時間判斷
IsTrue = datetime.datetime.strptime(
    "12:30:30.430000", "%H:%M:%S.%f") > datetime.datetime.strptime("12:30:30.440000", "%H:%M:%S.%f")
print(IsTrue)

# timedelta 進行計算
x = datetime.datetime.strptime("12:30:30.43000", "%H:%M:%S.%f")
print(x)

# 加上一秒
x += datetime.timedelta(0, 1)
print(x)

# 減去一秒
x -= datetime.timedelta(0, 1)
print(x)