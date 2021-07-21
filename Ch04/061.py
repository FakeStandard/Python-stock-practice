### 061 個股本益比
from urllib.request import urlopen
import sys
import json

date = sys.argv[1]
selecttype = sys.argv[2]

html = urlopen('http://www.tse.com.tw/exchangeReport/BWIBBU_d?response=json&date=' +
               date+'&selectType='+selecttype)

content = html.read().decode('utf-8')
jcontent = json.loads(content)
# 只取 data 欄位
data = jcontent['data']
# 迭代忽略 i[4] =='-'
data = [i for i in data if i[4] != '-']

# 爬出的資料格式
# 證券代號、證券名稱、殖利率、股利年度、本益比、股價淨值比、財報年/季

# sorted 對所有可迭代對象進行排序,參數(可迭代對象(iterable),比較函數(cmp),進行比較的元素,依照此元素進行排序(key),排序規則(reverse)True-降冪)
# 因為有千分位符,故比較時須先replace
EPS_list = sorted(data, key=lambda x: float(
    x[4].replace(',', '')), reverse=True)[:100]

print(EPS_list)
