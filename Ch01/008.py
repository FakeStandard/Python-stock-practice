# 008
# list comprehension -> 列表推導式
# [運算式 for 指定元素名稱 in 指定的列表]
x = [1, 2, 3, 4, 5]
# 將所有集合內的元素+1
y = [i+1 for i in x]
print(y)
# 將所有集合內的元素平方
y = [i**2 for i in x]
print(y)

# [運算式 for 指定元素名稱 in 指定的列表 if 特定條件]
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
print(y)
y = [i**2 for i in x if i != 3]
print(y)

# 從一維陣列變成二維陣列
y = [[i, i**2] for i in x if i != 3]
print(y)

# 從二維陣列中取得某個特定欄位
y = [i[0] for i in y]
print(y)
