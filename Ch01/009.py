# 009
# open 取用檔案(檔案名稱, 權限)
import os
file = open('123.txt','w+')
name = file.name
print(name)

str = [line for line in open('123.txt')]
print(str)

# 查詢檔案是否關閉, 回傳 boolean
IsClosed = file.closed
print(IsClosed)

# 查詢對檔案的權限
mode = file.mode
print(mode)

# 關閉檔案
file.close()

# 再查詢一次檔案是否關閉, 回傳 boolean
IsClosed = file.closed
print(IsClosed)

# 寫入檔案
file = open('123.txt', 'w+')
file.write('123456789\n1234568789')
file.close()

# 讀取檔案
file = open('123.txt', 'r')
str = file.read()
print(str)
file.close()

# 修改檔案名稱
# 要載入 os 套件, import os
os.rename('123.txt', '456.txt')

# 移除檔案
# 一樣須要載入 os 套件, import os
os.remove('456.txt')

# readline、readlines 讀取檔案行數
# readline 讀取一行
str1 = open('text_sample.txt').readline()
print(str1)
# readlines 讀取所有行, 存成 list 格式
str2 = open('text_sample.txt').readlines()
print(str2)