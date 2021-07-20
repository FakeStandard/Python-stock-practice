# 035
# 透過 matplotlib.finance 套件可繪至K線圖
# 但 Python 3.6 已經不支援, 故可手動安裝
# pip install https://github.com/matplotlib/mpl_finance/archive/master.zip
# 結果上述版本也被棄用,故找到下列安裝方式
# pip install --upgrade mplfinance
# https://github.com/matplotlib/mplfinance

# import mpl_finance
import mplfinance as mpf

import pandas

# 載入相關套件及函數
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from backtest_function import GetHistoryData

# 將日期和代碼變成參數帶入
date = sys.argv[1]
stockid = sys.argv[2]

# 取得成交資訊
Data = GetHistoryData(date, stockid)

# 定義相關變數
KBar = []
InitTime = datetime.datetime.strptime('090000000000', "%H%M%S%f")
Cycle = 60

# 日期.成交量.開盤價.最高價.最低價.收盤價
# 開始進行K線計算
for i in range(len(Data)):
    time = datetime.datetime.strptime(Data[i][0], "%H%M%S%f")
    price = float(Data[i][2])
    qty = int(Data[i][1])
    if len(KBar) == 0:
        KBar.append([mdates.date2num(InitTime),
                    qty, price, price, price, price])
    else:
        if time < InitTime + datetime.timedelta(0, Cycle):
            if price > KBar[-1][3]:
                KBar[-1][3] = price
            elif price < KBar[-1][4]:
                KBar[-1][4] = price
            KBar[-1][5] = price
            KBar[-1][1] += qty
        else:
            InitTime += datetime.timedelta(0, Cycle)
            KBar.append([mdates.date2num(InitTime),
                        qty, price, price, price, price])

print(KBar)

dfData = pandas.DataFrame(
    KBar, columns=['Date', 'Volume', 'Open', 'High', 'Low', 'Close'])

# dfData = pandas.DataFrame([
#     ['2021-02-01',70161939,595.00,612.00,587.00,611.00],
#     ['2021-02-02',80724207,629.00,638.00,622.00,632.00],
#     ['2021-02-03',59763227,638.00,642.00,630.00,630.00],
#     ['2021-02-04',47547873,626.00,632.00,620.00,627.00],
#     ['2021-02-05',57350831,638.00,641.00,631.00,632.00],
#     ['2021-02-17',115578402,663.00,668.00,660.00,663.00],
#     ['2021-02-18',54520341,664.00,665.00,656.00,660.00],
#     ['2021-02-19',51651844,656.00,657.00,647.00,652.00],
#     ['2021-02-22',39512078,660.00,662.00,650.00,650.00],
#     ['2021-02-23',52868029,641.00,643.00,633.00,641.00],
#     ['2021-02-24',80010637,627.00,636.00,625.00,625.00],
#     ['2021-02-25',45279276,636.00,636.00,628.00,635.00],
#     ['2021-02-26',137933162,611.00,618.00,606.00,606.00],
# ], columns=['Date', 'Volume', 'Open', 'High', 'Low', 'Close'])

dfData = dfData.set_index(pandas.to_datetime(dfData['Date']))

# 定義圖表物件
fig = plt.figure()
# 定義第一個圖案在圖表的位置
ax1 = fig.add_subplot(111)

# 資料處理成 mplfinance 可讀格式
# KBar.index = ['Date']
# KBar.columns = ['Close', 'High', 'Low', 'Open']

# 繪製K線圖
# mpf.plot(KBar, type='candle')
mpf.plot(dfData, type='candle')

# 定義 x 軸時間格式
hfmt = mdates.DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(hfmt)

plt.show()
