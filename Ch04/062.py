### 062 殖利率

from urllib.request import urlopen
import sys
import json

date = sys.argv[1]
selecttype = sys.argv[2]

html = urlopen('http://www.tse.com.tw/exchangeReport/BWIBBU_d?response=json&date=' +
               date+'&selectType='+selecttype)

content = html.read().decode('utf-8')

jcontent = json.loads(content)
data = jcontent['data']
data = [i for i in data if i[4] != '-']

# 爬出的資料格式
# 證券代號、證券名稱、殖利率、股利年度、本益比、股價淨值比、財報年/季

Dividend_list = sorted(data, key=lambda x: float(
    x[2].replace(',', '')), reverse=True)[:100]
print(Dividend_list)
