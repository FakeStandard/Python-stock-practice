# 046
# 1 分鐘 K 線進行計算的回測

import sys
from backtest_function import GetHistoryTAKBar, DayList
from talib.abstract import *

sid = sys.argv[1]

# 定義績效
TotalProfit = []

for date in DayList():
    # 取得 Talib 格式的 K 線
    TAKBar = GetHistoryTAKBar(date, sid)
    # 計算 MA 技術指標
    TAKBar['MA'] = MA(TAKBar, timeperiod=10, matype=1)
    # 計算 RSI 技術指標
    TAKBar['RSI'] = RSI(TAKBar, timeperiod=10)

    # 進場判斷
    Index = 0
    for i in range(1, len(TAKBar['time'])):
        # 定義策略須要的變數:價格、上一筆價格、MA、上一筆MA、RSI
        price = TAKBar['close'][i]
        lastprice = TAKBar['close'][i-1]
        ma = TAKBar['MA'][i]
        lastma = TAKBar['MA'][i-1]
        rsi = TAKBar['RSI'][i]

        # 當 RSI > 50 且價格向上突破 MA 進場做多
        if rsi > 50 and lastprice <= lastma and price > ma:
            Index = 1
            OrderTime = TAKBar['time'][i]
            OrderPrice = price
            break
        # 當 RSI < 50 且價格向下突破 MA 進場做空
        elif rsi < 50 and lastprice >= lastma and price < ma:
            Index = -1
            OrderTime = TAKBar['time'][i]
            OrderPrice = price
            break
        # 當日無進場
        elif i == len(TAKBar['time'])-1:
            print(date+' No Trade')

    # 若沒有進場,則不進行接下來的出場判斷
    if Index == 0:
        continue

    # 多單出場判斷
    if Index == 1:
        for j in range(i+1, len(TAKBar['time'])):
            # 定義策略須要的變數：價格、上一筆價格、MA、上一筆 MA
            price = TAKBar['close'][j]
            lastprice = TAKBar['close'][j-1]
            ma = TAKBar['MA'][j]
            lastma = TAKBar['MA'][j-1]

            # 當價格下向突破 MA 多單出場
            if lastprice >= lastma and price < ma:
                CoverTime = TAKBar['time'][j]
                CoverPrice = price
                break

            # 收盤強制出場
            elif j == len(TAKBar['time'])-1:
                CoverTime = TAKBar['time'][j]
                CoverPrice = price
        Profit = CoverPrice-OrderPrice
        TotalProfit += [Profit]
        print(sid, 'Buy OrderTime', OrderTime, 'OrderPrice', OrderPrice,
              'CoverTime', CoverTime, 'CoverPrice', CoverPrice, 'Profit', Profit)
    # 空單出場判斷
    elif Index == -1:
        for j in range(i+1, len(TAKBar['time'])):
            # 定義策略需要的變數 價格、上一筆價格、MA、上一筆MA
            price = TAKBar['close'][j]
            lastprice = TAKBar['close'][j-1]
            ma = TAKBar['MA'][j]
            lastma = TAKBar['MA'][j-1]
            # 當價格向上突破MA 空單出場
            if lastprice <= lastma and price > ma:
                CoverTime = TAKBar['time'][j]
                CoverPrice = price
                break
            # 收盤強制出場
            elif j == len(TAKBar['time'])-1:
                CoverTime = TAKBar['time'][j]
                CoverPrice = price
        Profit = OrderPrice-CoverPrice
        TotalProfit += [Profit]
        print(sid, 'Sell OrderTime', OrderTime, 'OrderPrice', OrderPrice,
              'CoverTime', CoverTime, 'CoverPrice', CoverPrice, 'Profit', Profit)

# 顯示總績效
print('Total Profit', sum(TotalProfit))
