### 029
# matplotlib.bar -> 長條圖(直方圖)
# add_subplot(總行數,總列數,第幾個圖表)
# ex:add_subplot(2,1,1) 表示該圖行為2行1列圖表中的第一個圖形
# 可縮寫成 add_subplot(211)

# 載入相關套件及函數
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from backtest_function import GetHistoryData

# # 定義圖表物件
# fig = plt.figure(1)

# # 定義第一張圖案在圖表的位置
# ax1 = fig.add_subplot(211)
# ax1.plot()

# # 定義第二章圖案在圖表的位置
# ax2 = fig.add_subplot(212)
# ax2.plot()

# 將日期及股票代碼變成參數帶入
date = sys.argv[1]
stockid = sys.argv[2]

# 取得成交資訊
Data = GetHistoryData(date, stockid)

# 定義相關變數
volume = []
InitTime = datetime.datetime.strptime('090000000000', "%H%M%S%f")
Cycle = 60

# 開始進行量能計算
for i in range(len(Data)):
    time = datetime.datetime.strptime(Data[i][0], "%H%M%S%f")
    qty = int(Data[i][3])
    if len(volume) == 0:
        volume.append([InitTime, qty])
    else:
        if time < InitTime + datetime.timedelta(0, Cycle):
            volume[-1][1] += qty
        else:
            InitTime += datetime.timedelta(0, Cycle)
            volume.append([InitTime, qty])

# 開始進行繪圖
# 取得轉換時間字串至時間格式
Time = [datetime.datetime.strptime(line[0], "%H%M%S%f") for line in Data]
# 將 datetime 時間格式轉換為繪圖專用的時間格式,透過 mdates.date2num函數
Time1 = [mdates.date2num(line) for line in Time]
# 價格由字串轉成數值
Price = [float(line[2]) for line in Data]

# 定義圖表位置
fig = plt.figure(1)
ax1 = fig.add_subplot(211)

# 定義 title
plt.title('Price & Volume Line')

# 繪製價格折線圖
ax1.plot_date(Time1, Price, 'k-')

# 取得轉換時間字串至時間格式
QTime = [line[0] for line in volume]
# 將 datetime 時間格式轉換為繪圖專用的時間格式,透過 mdates.date2num 函數
QTime1 = [mdates.date2num(line) for line in QTime]
# 取出量能的list
QValue = [line[1] for line in volume]

# 定義第二張圖表的位置
ax2 = fig.add_subplot(212)
# 透過長條圖進行量能繪製
ax2.bar(QTime, QValue, width=0.0005)
# 也可透過直線圖繪製
# ax2.vlines(QTime, [0], QValue)

# bar 參數 (x軸物件,y軸物件,寬度)
# vlines 參數 (x軸物件, y軸起始點, y軸物件)

# 定義 x 軸
hfmt = mdates.DateFormatter('%H:%M:%S')
ax1.xaxis.set_major_formatter(hfmt)
ax2.xaxis.set_major_formatter(hfmt)

plt.show()
