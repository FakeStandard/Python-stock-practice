# 075
import datetime
import function
import indicatory

Date = datetime.datetime.now().strftime("%Y%m%d")
Sid = '3000'
KBar1M = indicatory.KBar(date=Date)
for i in function.getSIDMatch(Date, Sid):
    time = datetime.datetime.strptime(Date+i[0], '%Y%m%d%H:%M:%S>%f')
    price = float(i[2])
    qty = int(i[3])
    check = KBar1M.Add(time, price, qty)
    open = KBar1M.GetOpen()
    high = KBar1M.GetHigh()
    low = KBar1M.GetLow()
    close = KBar1M.GetClose()
    print(open, high, low.close)
