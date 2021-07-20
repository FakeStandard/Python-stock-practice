# 018

# 函數定義
# def 函數名稱(輸入值/參數):
#   縮排(函數執行內容)
#   ...
#   return 輸出值/返回值


# 無參數函數
def printHello():
    print('hello world')


printHello()

# 具有兩個參數的函數
def mySum(x, y):
    rs = 0
    for i in range(x, y+1):
        rs += i
    return rs


# 從 4 加到 10
sum = mySum(4, 10)
print(sum)
