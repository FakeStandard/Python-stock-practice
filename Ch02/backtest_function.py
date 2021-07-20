# 直接讀取 csv
def GetHistoryData(date, sid):
    HData = open('Stock_Tick/'+date+'_Stock.csv').readlines()
    MData = [line.strip('\n').split(',') for line in HData]
    MData_1 = [line for line in MData if line[1] == sid]
    return MData_1