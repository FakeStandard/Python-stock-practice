# 031

# 載入相關套件及函數
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from backtest_function import GetHistoryData

# 將日期及股票代碼變成參數帶入
date = sys.argv[1]
stockid = sys.argv[2]

# 取得成交資訊
Data = GetHistoryData(date, stockid)

# 定義相關變數
BSpower = [[datetime.datetime.strptime(Data[0][0], "%H%M%S%f"), 0]]

# 開始進行內外盤計算
for i in range(1, len(Data)):
    time = datetime.datetime.strptime(Data[i][0], "%H%M%S%f")
    price = float(Data[i][2])
    lastprice = float(Data[i-1][2])
    qty = int(Data[i][3])

    if price > lastprice:
        BSpower.append([time, BSpower[-1][1]+qty])
    elif price < lastprice:
        BSpower.append([time, BSpower[-1][1]-qty])
# print(BSpower)

# 開始繪圖
# 取得轉換時間字串至時間格式
Time = [datetime.datetime.strptime(line[0], "%H%M%S%f") for line in Data]
# 將 datetime 時間格式轉換為繪圖專用的時間格式,透過 mdates.date2num 函數
Time1 = [mdates.date2num(line) for line in Time]
# 價格由字串轉成數值
Price = [float(line[2]) for line in Data]


# 定義圖表物件
fig = plt.figure()
ax1 = fig.add_subplot(211)

# 定義 title
plt.title('Price & BSpower Line')

# 繪製價格折線圖
ax1.plot_date(Time1, Price, 'k-')

# 取得轉換時間字串至時間格式
STime = [line[0] for line in BSpower]
print(STime)
# 將 datetime 時間格式轉換為繪圖專用的時間格式,透過mdates.date2num 函數
STime1 = [mdates.date2num(line) for line in STime]
# 取出量能的list
SValue = [line[1] for line in BSpower]

# 定義第二章圖案在圖表的位置
ax2 = fig.add_subplot(212)
# 繪製內外盤量走勢圖
ax2.plot_date(STime1, SValue, 'r-')

# 定義 x 軸
hfmt = mdates.DateFormatter('%H:%M:%S')
ax1.xaxis.set_major_formatter(hfmt)
ax2.xaxis.set_major_formatter(hfmt)

# 顯示繪製圖表
plt.show()
