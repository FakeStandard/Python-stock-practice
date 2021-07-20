# 042
# 安裝套件
# pip install TA-Lib
import talib
# 產出套件內全部的函數,*表示所有函數
from talib.abstract import *

# Function API(函數API)
# Abstract API(抽象API)

from backtest_function import GetHistoryTAKBar

# 查看每個指標所擁有的參數以及輸出內容

# 移動平均線
# >>> MA
# output
# {'name': 'MA', 'group': 'Overlap Studies', 'display_name': 'Moving average', 'function_flags': ['Output scale same as input'], 'input_names': OrderedDict([('price', 'close')]), 'parameters': OrderedDict([('timeperiod', 30), ('matype', 0)]), 'output_flags': OrderedDict([('real', ['Line'])]), 'output_names': ['real']}

TAKBar = GetHistoryTAKBar('20180903','2330')
MAValue = MA(TAKBar)
# print(MAValue[:30])

MAValue = MA(TAKBar,timeperiod=10)
# print(MAValue[:20])

# 布林通道
# >>> BBANDS

upper,middle,lower = BBANDS(TAKBar)
# print(upper[:20])
# print(middle[:20])
# print(lower[:20])

TAKBar['upper'],TAKBar['middle'],TAKBar['lower'] = BBANDS(TAKBar,timeperiod=10)
print(TAKBar['upper'][:20])
print(TAKBar['middle'][:20])
print(TAKBar['lower'][:20])

# output: dict_keys(['time', 'open', 'high', 'low', 'close', 'volume', 'upper', 'middle', 'lower'])
print(TAKBar.keys())

# 拋物線轉向
# >>> SAR

# 指數平滑異同移動平均線
# >>> MACD

