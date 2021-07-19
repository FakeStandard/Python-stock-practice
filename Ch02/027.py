### 027

# 載入相關套件及函數
import sys
import datetime
from backtest_function import GetHistoryData

# 將日期和股票代碼變成參數帶入
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

# 開始進行 MA 計算
for i in Data:
    # 取得交易時間
    time = datetime.datetime.strptime(i[0], "%H%M%S%f")
    # 取得成交價
    price = float(i[2])

    # 不太理解平均值算法的基準是(?)
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

    # 計算平均值
    MAValue = float(sum(MArray))/len(MArray)
    # 將結果添加於陣列中
    MA.append([time.strftime("%H:%M:%S"), MAValue])

print(MA)
