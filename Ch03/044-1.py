# 044-1
# 一天回測
import sys
from backtest_function import GetHistoryData

date = sys.argv[1]
stockid = sys.argv[2]

Data = GetHistoryData(date, stockid)

# 取得進出場時間以及價格
OrderTime = Data[0][0]
OrderPrice = float(Data[0][2])
CoverTime = Data[-1][0]
CoverPrice = float(Data[-1][2])

print(stockid, 'Buy OrderTime', OrderTime, 'OrderPrice', OrderPrice, 'CoverTime',
      CoverTime, 'CoverPrice', CoverPrice, 'Profit', CoverPrice-OrderPrice)
