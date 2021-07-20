# 041
import datetime
import matplotlib.dates as mdates
import numpy
import backtest_function
Data = backtest_function.GetHistoryData('20180903', '2330')

KBar = []
InitTime = datetime.datetime.strptime('090000000000', "%H%M%S%f")
Cycle = 600

# 日期.開盤價.最高價.最低價.收盤價.成交量
for i in range(len(Data)):
    time = datetime.datetime.strptime(Data[i][0], "%H%M%S%f")
    price = float(Data[i][2])
    qty = int(Data[i][1])

    if len(KBar) == 0:
        KBar.append([mdates.date2num(InitTime),
                     price, price, price, price, qty])
    else:
        if time < InitTime+datetime.timedelta(0, Cycle):
            if price > KBar[-1][2]:
                KBar[-1][2] = price
            elif price < KBar[-1][3]:
                KBar[-1][3] = price
            KBar[-1][4] = price
            KBar[-1][5] += qty
        else:
            InitTime += datetime.timedelta(0, Cycle)
            KBar.append([mdates.date2num(InitTime),
                        price, price, price, price, qty])

print(KBar[0])

# Value 必須透過 numpy 套件中的 array 函數進行定義
TAKBar = {}
TAKBar['time'] = numpy.array([line[0] for line in KBar])
TAKBar['open'] = numpy.array([line[1] for line in KBar])
TAKBar['high'] = numpy.array([line[2] for line in KBar])
TAKBar['low'] = numpy.array([line[3] for line in KBar])
TAKBar['close'] = numpy.array([line[4] for line in KBar])
TAKBar['volume'] = numpy.array([line[5] for line in KBar])

print(TAKBar)
