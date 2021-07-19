# 010
# 字串處理
# len - 字串長度
str = "I am a software engineer."
len = len(str)
print(len)

# join - 將元素透過特定符號組合
seq = "\t"
cc = ('1', '2', '3', '4')
seq = seq.join(cc)
print(seq)

# strip - 將特定字元從字首字尾中移除
str = " aa i am a software engineer rr "
print(str)
str = str.strip()
print(str)
str = str.strip("a")
print(str)
str = str.strip("r")
print(str)

# lstrip 將特定字元從字首中移除
str = str.lstrip(" i")
print(str)

# rstrip 將特定字元從字尾中移除
str = str.rstrip(" ")
str = str.rstrip("engineer")
print(str)

# 將任何英文字母轉換大小寫
str = "I am A SoftWare EngiNeer"
str = str.swapcase()
print(str)

# 將英文字母轉成大寫
str = str.lower()
print(str)

# 將英文字母轉乘小寫
str = str.upper()
print(str)

# 查看字串中的最大值
max = max(str)
print(max)

# 查看字串中的最小值
min = min(str)
print(min)

# zfill - 將字串透過 0 填滿至特定寬度
strFill = "AAA"
strFill = strFill.zfill(15)
print(strFill)

# replace - 取代字串中特定字元
strRe = "NORGODFKOPW"
strRe = strRe.replace('GOD', 'ABC')
print(strRe)

# split 將字串依照特定符號進行分割
str = "111,222,333,444,555,666,777,888"
list = str.split(',')
print(list)

# splitlines - 將字串依照換行符號進行分割
str = "111,222,333,444,555,666,777,888\n123\n456789\n484984\n\n151"
str = str.splitlines()
print(str)
