### 028
# pyplot.subplot 可在一張圖內繪製多個圖像

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
MArray = []
MA = []
MAValue = 0
InitTime = datetime.datetime.strptime('090000000000', "%H%M%S%f")
Cycle = 60
MAlen = 10

# 開始進行MA計算
for i in Data:
    time = datetime.datetime.strptime(i[0], "%H%M%S%f")
    price = float(i[2])

    if len(MArray) == 0:
        MArray += [price]
    else:
        if time < InitTime + datetime.timedelta(0, Cycle):
            MArray[-1] = price
        else:
            if len(MArray) == MAlen:
                MArray = MArray[1:]+[price]
            else:
                MArray += [price]
            InitTime += datetime.timedelta(0, Cycle)

    MAValue = float(sum(MArray))/len(MArray)
    MA.append(MAValue)

# 開始進行繪圖
# 取得轉換時間字串至時間格式
Time = [datetime.datetime.strptime(line[0], "%H%M%S%f") for line in Data]
# 將 datetime 時間格式轉換為繪圖專用的時間格式,透過 mdates.date2num 函數
Time1 = [mdates.date2num(line) for line in Time]
# 價格由字串轉數值
Price = [float(line[2]) for line in Data]

# 定義圖表物件
ax = plt.figure(1)  # 第一張圖片
ax = plt.subplot(111)  # 該圖片僅一個圖案
# 可縮寫為
# fig, ax = plt.subplots()

# 定義 title
plt.title('Price&MA Line')

# 繪製價格折線圖
ax.plot_date(Time1, Price, 'k-')
# 繪製 MA 折線圖
ax.plot_date(Time1, MA, 'r-')

# 定義 x 軸
hfmt = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(hfmt)

# 顯示繪製圖表
plt.show()

# 紅線為 MA 線