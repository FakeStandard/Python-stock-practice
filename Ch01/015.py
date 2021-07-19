# 015
# 資料分割與合併
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[0])
print(x[1])
print(x[-2])

# 使用 : 取得連續值
print(x[:3])
print(x[3:])
# Error -> TypeError: 'builtin_function_or_method' object is not subscriptable
# print[x[:-2]]
# print(x[-2:])

# 取得特定倍數索引值的間格的值, 比如索引為 2 的倍數的值
print(x[::2])
print(x[::3])

# 分割
# [自訂變數 for 自訂變數 in 指定 list if 條件判斷句]
y = [i for i in x if i > 5]
print(y)

# 合併
# +
x = [1, 2, 3]
y = [4, 5, 6]
print(x+y)

# append
x.append(100)
print(x)

# extend
x.extend(y)
print(x)