# 047-1

import sys
import time
import datetime
import numpy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from talib.abstract import *
from backtest_function import GetHistoryTAKBar, DayList

date = sys.argv[1]
stockid = sys.argv[2]

# 取得 TAlib 格式的 K 線
TAKBar = GetHistoryTAKBar(date, stockid)
# 計算 MA 技術指標
TAKBar['MA'] = MA(TAKBar, timeperiod=10, matype=1)

Time1 = mdates.date2num(TAKBar['time'])

# 定義圖表物件
ax = plt.subplot(111)

# 繪製圖案
ax.plot_date(Time1, TAKBar['close'], 'k-')
ax.plot_date(Time1, TAKBar['MA'], 'r-')

# 定義 Title
plt.title('Stock '+stockid+' Price MA Line')

# 定義x軸
hfmt = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hfmt)

# 顯示繪製圖表
plt.show()