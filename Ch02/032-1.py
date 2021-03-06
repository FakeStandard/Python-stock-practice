# 032-1

# 載入相關套件和函數
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from backtest_function import GetHistoryData

# 將日期及股票代號變成參數帶入
date = sys.argv[1]
stockid = sys.argv[2]

# 取得成交資訊
Data = GetHistoryData(date, stockid)

# 定義相關變數
BigTrade = []
BigValue = 10000000

# 開始進行內外盤計算
for i in range(1, len(Data)):
    time = datetime.datetime.strptime(Data[i][0], "%H%M%S%f")
    price = float(Data[i][2])
    qty = int(Data[i][3])
    value = price*1000*qty

    if value > BigValue:
        BigTrade.append([time, price])
# print(BigTrade)

# 開始進行繪圖
# 取得轉換時間字串至時間格式
Time = [datetime.datetime.strptime(line[0], "%H%M%S%f") for line in Data]
# 將 datetime 時間格式轉換為繪圖專用的時間格式,透過 mdates.date2num 函數
Time1 = [mdates.date2num(line) for line in Time]
# 價格由字串轉成數值
Price = [float(line[2]) for line in Data]

# 定義圖表物件
ax = plt.subplot(111)

# 定義 title
plt.title('Price & BigTrade Line')

# 繪製價格折線圖
ax.plot_date(Time1, Price, 'k-')

# 繪製標記大單位置
if len(BigTrade) != 0:
    # 取得時間字串轉換至時間格式
    STime = [line[0] for line in BigTrade]
    # 將 datetime 時間格式轉換為繪圖專用的時間格式,透過 mdates.date2num 函數
    STime1 = [mdates.date2num(line) for line in STime]
    # 取出量能的list
    SValue = [line[1] for line in BigTrade]
    # 繪製出折線圖
    ax.plot_date(STime1, SValue, 'b.', markersize='8')

# 定義 x 軸
hfmt = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(hfmt)

# 顯示繪製圖表
plt.show()
