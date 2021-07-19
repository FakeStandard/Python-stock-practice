# 繪製價格折線圖
# 繪製時間序列的函數 -> plot_date
# 一般繪製的函數 -> plot
# plot 的 LineStyle(繪製線)
# . 點圖
# - 實線圖
# -. 點線圖
# : 點圖
# -- 虛線圖
# o 原點
# s 方塊
# ^,>,< 向上三角形, 向右三角形, 向左三角形
# 空白鍵 空白
# None 空值

# 載入相關套件
from os import get_inheritable
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from backtest_function import GetHistoryData

# 將日期以及股票代碼變成參數帶入
date = sys.argv[1]
stockid = sys.argv[2]

# 取得成交資訊
Data = GetHistoryData(date, stockid)

# 取得轉換時間字串至時間格式
Time = [datetime.datetime.strptime(line[0], "%H%M%S%f") for line in Data]

# 將 datetime 時間格式轉換為繪圖專用的時間格式,透過 mdates.date2num 函數
Time1 = [mdates.date2num(line) for line in Time]

# 價格由字串轉數值
Price = [float(line[2]) for line in Data]

# 定義圖表物件
ax = plt.figure(1)  # 第一張圖片
ax = plt.subplot(111)  # 該張圖片僅一個圖案
# 以上兩行可縮寫成一行
# fig, ax = plt.subplots()

# 繪製圖案
# plot_date(x軸物件, y軸物件, 線風格)
ax.plot_date(Time1, Price, 'k-')

# 定義 title
plt.title('Stock '+stockid+' Price Line')

# 定義 x 軸
hfmt = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hfmt)

# 顯示繪製圖表
plt.show()

# 執行 python 025.py 20180903 3008 即跑出圖