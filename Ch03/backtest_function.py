# backtest 回測(日期, 股票代號)
import numpy
import datetime
import matplotlib.dates as mdates
from os import listdir

# 直接讀取 csv
def GetHistoryData(date, sid):
    HData = open('Stock_Tick/'+date+'_Stock.csv').readlines()
    MData = [line.strip('\n').split(',') for line in HData]
    MData_1 = [line for line in MData if line[1] == sid]
    return MData_1


# 使用 numpy 套件的 array 函數定義
def GetHistoryTAKBar(date, stockid):
    Data = GetHistoryData(date, stockid)
    KBar = ConversionData(Data)
    # Value 必須透過 numpy 套件中的 array 函數進行定義
    TAKBar = {}

    # TAKBar['time'] = numpy.array([line[0] for line in KBar])
    TAKBar['time'] = numpy.array([line[0] for line in KBar])
    TAKBar['open'] = numpy.array([line[1] for line in KBar])
    TAKBar['high'] = numpy.array([line[2] for line in KBar])
    TAKBar['low'] = numpy.array([line[3] for line in KBar])
    TAKBar['close'] = numpy.array([line[4] for line in KBar])
    TAKBar['volume'] = numpy.array([line[5] for line in KBar])
    return TAKBar

# 將資料格式轉換成=>日期.開盤價.最高價.最低價.收盤價.成交量
def ConversionData(data):
    arr = []
    InitTime = datetime.datetime.strptime('090000000000', "%H%M%S%f")
    Cycle = 60

    # InitTime 不要用 mdates.date2num() 轉繪圖時間格式, 時間格式有問題會無法繪製
    for i in range(len(data)):
        time = datetime.datetime.strptime(data[i][0], "%H%M%S%f")
        price = float(data[i][2])
        qty = int(data[i][1])

        if len(arr) == 0:
            arr.append([InitTime,
                        price, price, price, price, qty])
        else:
            if time < InitTime+datetime.timedelta(0, Cycle):
                if price > arr[-1][2]:
                    arr[-1][2] = price
                elif price < arr[-1][3]:
                    arr[-1][3] = price
                arr[-1][4] = price
                arr[-1][5] += qty
            else:
                InitTime += datetime.timedelta(0, Cycle)
                arr.append([InitTime,
                            price, price, price, price, qty])
    return arr

# 長期(多天數)回測
def DayList(path='Stock_Tick'):
    data_list = listdir(path)
    day_list = [i[:8] for i in data_list]
    return day_list
