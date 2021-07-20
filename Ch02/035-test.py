# 035-test

import pandas
import mplfinance as mpf
import sys
import datetime
import matplotlib.dates as mdates
from backtest_function import GetHistoryData

data = sys.argv[1]
stockid = sys.argv[2]

Data = GetHistoryData(data, stockid)

KBar = []
InitTime = datetime.datetime.strptime('090000000000', "%H%M%S%f")
Cycle = 600


# 日期.成交量.開盤價.最高價.最低價.收盤價

for i in range(len(Data)):
    time = datetime.datetime.strptime(Data[i][0], "%H%M%S%f")
    price = float(Data[i][2])
    qty = int(Data[i][1])

    if len(KBar) == 0:
        KBar.append([mdates.date2num(InitTime),
                    qty, price, price, price, price])
    else:
        if time < InitTime+datetime.timedelta(0, Cycle):
            if price > KBar[-1][3]:
                KBar[-1][3] = price
            elif price < KBar[-1][4]:
                KBar[-1][4] = price
            KBar[-1][5] = price
            KBar[-1][1] += qty
        else:
            InitTime += datetime.timedelta(0, Cycle)
            KBar.append([mdates.date2num(InitTime), qty,
                        price, price, price, price])

print(KBar)

dfData = pandas.DataFrame(
    KBar, columns=['Date', 'Volume', 'Open', 'High', 'Low', 'Close'])

dfData = dfData.set_index(pandas.to_datetime(
    dfData['Date'], unit='s', utc=True))

# 設置樣式
mc = mpf.make_marketcolors(up='r',
                           down='g',
                           edge='',
                           wick='inherit',
                           volume='inherit')
s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)

mpf.plot(dfData, type='candle', title='K Line',
         volume=True, ylabel_lower='Shares',
         datetime_format='%Y-%m-%d %H:%M:%S', xrotation=45,style=s)

# 時間怪怪的, 都是一樣的時間 = =...


