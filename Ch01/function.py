# 外部函式庫
def cumsum(x):
    y = []
    sum = 0
    for i in x:
        sum += i
        y.append(sum)
    return y
