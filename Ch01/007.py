# 007
# 操作 tuple.list.dictionary
# tuple 定義後不可被更動內部值. list 則可以
# dictionary 可增加鍵值(索引值)
x = [1, 2, 3]
x[2] = 4
print(x)

x = (1, 2, 3)
# x[2] = 4
# TypeError: 'tuple' object does not support item assignment
# print(x)

# tuple 用小括號定義
# 一維 tuple
x = (1, 2, 3, 4, 5)
print(x)

# 二維 tuple
x = ((1, 2), (3, 4), (5, 6))
print(x)

# 一行中定義多變數
x, y = (1, 2, 3), (4, 5, 6)
print(x)
print(y)

# 刪除 tuple 變數(del)
# del x
# NameError: name 'x' is not defined
# print(x)

# tuple 取值
x = ((1, 2), (3, 4), (5, 6))
print(x[0])
print(x[1])
print(x[0][0])

# tuple 計算 -> 組合或複製
x = (1, 2, 3)
y = (4, 5, 6)
print(x+y)
print(x*3)

# 函數比較
print(max(x))
print(min(y))

# 判斷是否存在,回傳 boolean
print(3 in x)
print(3 in y)

# 迴圈
for i in x:
    print(i)

# list 用中括號定義
x = [1, 2, 3, 4, 5, 6]
print(x)
x = [[1, 2], [3, 4], [5, 6]]
print(x)

# 一行中定義多變數
x, y = [1, 2, 3], [4, 5, 6]
print(x)
print(x)

# 刪除(del)
# del x
# NameError: name 'x' is not defined
# print(x)

# 取值
x = [1, 2, 3]
print(x[0])
print(x[1])

y = [[1, 2], [3, 4], [5, 6]]
print(y[0])
print(y[0][0])

# 計算 -> 組合或複製
x, y = [1, 2, 3], [4, 5, 6]
print(x+y)
print(y*3)

# 函數應用
# append 賦值
x = [1, 2, 3, 4, 5]
x.append(100)
print(x)

# count 計算項目再 list 中有幾個
print(x.count(100))
print(x.count(101))

# extend 將多個 list 彙整起來
x.extend([101, 102])
print(x)
y = [103, 104, 105]
x.extend(y)
print(x)

# index 取得特定項目再 list 中的位置(索引值)
print(x.index(105))
print(x.index(1))

# remove 刪除指定項目
x.remove(100)
print(x)

# reverse 反轉 list
x.reverse()
print(x)

# sort 由小到大排序 list, 若由大到小則 sort 完後再 reverse
y = [5, 6, 1, 8, 9, 0, 7, 4, 3, 2]
print(y)
y.sort()
print(y)
y.reverse()
print(y)

# 判斷項目是否存在於 list 中, 返回 boolean
print(5 in y)
print(11 in y)

# 迴圈
for i in y:
    print(i)

# dictionary 用大括號定義
x = {'one': 123, 'two': 456, 'three': 789}
print(x)

# 刪除 dictionary 變數(del)
# del x
# NameError: name 'x' is not defined
# print(x)

# dictionary 取值, 只可透過 index 取值
print(x['one'])
print(x['two'])

# 沒有透過 index 取值則會發生錯誤 -> KeyError: 0
# print(x[0])

# 函數應用
# len 查看物件長度
print(len(x))

# copy 複製物件
y = x.copy()
print(x)
print(y)

# clear 清除物件內容值, dictionary 變數還是存在
x.clear()
print(x)
print(y)

# 透過 item 將 dictionary 轉換為 list
z = y.items()
# output: dict_items([('one', 123), ('two', 456), ('three', 789)])
print(z)

# 透過 keys 函數取出 dictionary 內所有的 key
# output: dict_keys(['one', 'two', 'three'])
print(y.keys())
