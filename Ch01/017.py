# 017

# 基本語法
# for 迴圈變數 in 向量:
#   運算式

# break.continue.pass

for i in 1, 2, 3, 4:
    print('No.', i)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in x:
    print('No.', i)

for i in x[::2]:
    print('No.', i)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = 0
for i in x:
    y += i
    print(y)

y = 0
for i in x:
    if i == 7:
        continue
    y += i
    print(y)

# 基本語法
# while 判斷式:
#   運算式

x = 0
while x <= 7:
    print(x)
    x += 1

print(x)

# 無窮迴圈
# x = 0
# while 1:
#     print(x)
#     x += 1

x = 1
y = 0
while x <= 10:
    y += x
    x += 1

print(y)

# continue -> 跳離此次循環,繼續進行下次循環
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue
    print(x)

# break -> 直接跳離迴圈
# pass -> 不執行任何動作,用以編寫空迴圈主體