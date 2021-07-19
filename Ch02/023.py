### 023
# 取得資料
HData = open('Stock_Tick/20180919_Stock.csv').readlines()
print(HData[:3])

# 將每行行末的換行符號去除
[line.strip('\n') for line in HData][:3]
print(HData[:3])

# 將資料透過逗點分隔
[line.split(',') for line in HData]

# 將上述兩個動作合併且儲存成 MData
MData = [line.strip('\n').split(',') for line in HData]
print(MData[:3])

# 進行資料篩選,取德 10 點以前的資料
MData_1 = [line for line in MData if int(line[0]) <= 100000000000]

# 取最後十筆
print(MData_1[-10:])

# 取得特定商品資訊
MData_2 = [line for line in MData if line[1] == '2330']

# 取得前十筆
print(MData_2[:10])

# 使用自定義函數
import backtest_function
Data = backtest_function.GetHistoryData('20180903', '2330')
print(Data[0])

# 或者
# from backtest_function import GetHistoryData
# Data = GetHistoryData('20180903', '2330')
# print(Data[0])

# 測試
import hello
hello.say()