### 005
import math
import random

# +.-.*./
print(1+2)
print(7-4)
print(4*3)
print(21/3)
print(21/4)
print(21.0/4)

# 變數運算
x = 2
y = 5
print(x+y)

# 兩數相除取商數
# ex1
x = 14.0
y = 3
print(x/y)
# ex2
x = 14.0
y = 3
print(x//y)

# 餘數(%)
x = 30
y = 10
print(x % y)

y = 12
print(x % y)

x = 5
y = 3
print(x % y)

# 次方
# 表達: x 的 y次方 -> x**y
# 2^10 -> x**10
print(2**10)

# 亂數(Random)
# IDLE Shell 載入Random套件指令 -> >>> import random
# Add import random command to the top of script
a = random.randint(0, 99)
b = random.randint(0, 99)
# 隨機產生 0-101 中 2 的倍數
c = random.randrange(0, 101, 2)
d = random.randrange(0, 101, 2)
print(a)
print(b)
print(c)
print(d)

# 轉換數值型態
# 無條件捨去小數位
a = int(3.1)
print(a)
a = float(3)
print(a)
a = float(3.1)
print(a)

# 字串轉數值
x = "2.111"
y = float(x)
print(y)

# 四捨六入五成雙(round)
# 預設捨去位數為 0
x = round(4.5678)
print(x)
# 捨去位數指定 2 位
x = round(4.5678, 2)
print(x)
x = round(4.15, 1)
print(x)
x = round(3.15, 1)
print(x)

# 小於等於的最大整數(floor)
# IDLE Shell 載入math套件指令 -> >>> import math
# Add import math command to the top of script
x = math.floor(4.56)
print(x)
x = math.floor(4)
print(x)
x = math.floor(-4.123)
print(x)

# 大於等於的最小正數(ceil)
# IDLE Shell 載入math套件指令 -> >>> import math
# Add import math command to the top of script
x = math.ceil(4)
print(x)
x = math.ceil(4.1)
print(x)
x = math.ceil(-3)
print(x)
x = math.ceil(-3.3)
print(x)

# 開根號
# IDLE Shell 載入math套件指令 -> >>> import math
# Add import math command to the top of script
x = math.sqrt(16)
print(x)
x = math.sqrt(81)
print(x)
x = math.sqrt(3)
print(x)

# 絕對值
x = abs(100)
print(x)
x = abs(-100)
print(x)

# 指數函數(exp)
# IDLE Shell 載入math套件指令 -> >>> import math
# Add import math command to the top of script
x = math.exp(2)
print(x)
x = math.exp(10)
print(x)

# 對數函數(log)
# IDLE Shell 載入math套件指令 -> >>> import math
# Add import math command to the top of script
# log or log10, log-> 以e為底的對數
x = math.log(4)
print(x)
x = math.log(6)
print(x)

# 三角函數(sin.cos.tan)
# IDLE Shell 載入math套件指令 -> >>> import math
# Add import math command to the top of script
x = math.sin(10)
y = math.cos(10)
z = math.tan(10)
print(x)
print(y)
print(z)

# 最大值
x = max(-1, 1, 2, 3, 4, 5, 6, 7)
print(x)
y = (-1, 1, 2, 3, 4, 5, 6, 7)
print(max(y))

# 最小值
x = min(-1, 0, 1, 2, 3, 4, 5, 6, 7)
print(x)
y = (-1, 0, 1, 2, 3, 4, 5, 6, 7)
print(min(y))
