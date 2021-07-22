import tailer
from urllib.request import urlopen
import json,time,datetime

# 持續取得指定股票代碼的成交資訊
def getSIDMatch(Date,sid,BrokerID="capital",DataPath="C:/Data/"):
    for i in tailer.follow(open(DataPath+BrokerID+'/'+Date+'/'+sid+'_Match.txt'),0):
        j=i.strip('\n').split(',')
        yield j

# 取得指定股票代碼的最新一筆成交資訊
def getLastSIDMatch(Date,sid,BrokerID="capital",DataPath="C:/Data/"):
    tmpfiledata=open(DataPath+BrokerID+'/'+Date+'/'+sid+'_Match.txt').readlines()
    tmpfiledata.reverse()
    for i in tmpfiledata:
        j=i.strip('\n').split(',')
        return j