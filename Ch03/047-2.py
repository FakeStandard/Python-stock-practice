### 047-2

import sys,datetime,numpy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from talib.abstract import *
from backtest_function import GetHistoryTAKBar

date=sys.argv[1]
stockid=sys.argv[2]

# 取得 TALib 格式的 K線
TAKBar=GetHistoryTAKBar(date,stockid)
# 計算 MA 技術指標
TAKBar['MA'] = MA(TAKBar,timeperiod=10,matype=1)
# 計算 RSI 技術指標
TAKBar['RSI'] = RSI(TAKBar,timeperiod=10)

Time1 = mdates.date2num(TAKBar['time'])

#定義圖表物件-by 1
ax = plt.subplot(211)

#繪製圖案
ax.plot_date(Time1, TAKBar['close'], 'k-')
ax.plot_date(Time1, TAKBar['MA'], 'r-')

#定義title
plt.title('Stock '+stockid+' Price MA Line')

#定義圖表物件-by2
ax1 = plt.subplot(212)

#繪製圖案
ax1.plot_date(Time1, TAKBar['RSI'], 'r-')
ax1.plot_date(Time1, numpy.repeat(50,len(Time1)), 'y-')

#定義x軸
hfmt= mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hfmt)

#顯示繪製圖表
plt.show()

