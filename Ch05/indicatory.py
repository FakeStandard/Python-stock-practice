import numpy
import datetime

# K 線指標 class
# 參數週期


class KBar():
    # 建構子
    def __init__(self, date, cycle=1):
        self.Cycle = datetime.timedelta(minutes=cycle)
        self.Time = datetime.datetime.strptime(
            date+'090000', '%Y%m%d%H%M%S')-(self.Cycle*2)
        self.Open = numpy.array([])
        self.High = numpy.array([])
        self.Low = numpy.array([])
        self.Close = numpy.array([])
        self.Volume = numpy.array([])
    # 填入即時報價

    def Add(self, time, price, qty):
        # 沒有換分鐘
        if time < self.Time+self.Cycle:
            self.Close[-1] = price
            self.Volume[-1] += qty
            if price > self.High[-1]:
                self.High[-1] = price
            elif price < self.Low[-1]:
                self.Low[-1] = price
            return 0
        # 穿越指定時間週期 新增一根K棒
        elif time >= self.Time+self.Cycle:
            while time >= self.Time+self.Cycle:
                self.Time += self.Cycle
            self.Open = numpy.append(self.Open, price)
            self.High = numpy.append(self.High, price)
            self.Low = numpy.append(self.Low, price)
            self.Close = numpy.append(self.Close, price)
            self.Volume = numpy.append(self.Volume, qty)
            return 1
    # 取得開盤價陣列

    def GetOpen(self):
        return self.Open
    # 取得最高價陣列

    def GetHigh(self):
        return self.High
    # 取得最低價陣列

    def GetLow(self):
        return self.Low
    # 取得收盤價陣列

    def GetClose(self):
        return self.Close
