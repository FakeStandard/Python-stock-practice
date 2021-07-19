# 016
# 邏輯判斷式與條件判斷式

# 邏輯判斷式

# >,>=
x = 5
print(x > 5)
print(x >= 5)

# <,<=
x = 10
print(x < 10)
print(x <= 10)

# =,!=
x = 10
y = 11
print(x == y)
print(x != y)

# and
x = 10
y = 11
print(x == 9 and y == 11)
print(x == 10 and y == 11)

# or
x = 5
y = 4
print(x == 5 or y == 5)
print(x == 4 or y == 4)
print(x == 6 or y == 6)
print(x == 5 or y == 4)

# 條件判斷式
# if-else
x = 10
if x == 10:
    x += 10
    x += 5
else:
    x -= 10
print(x)

# if-elif
x = 10
if(x == 9):
    x += 10
elif x == 10:
    x -= 10
else:
    x *= 2
print(x)
