### 063 股價淨值比
from urllib.request import urlopen
import sys
import json

date = sys.argv[1]
selecttype = sys.argv[2]

html=urlopen('http://www.tse.com.tw/exchangeReport/BWIBBU_d?response=json&date='+date+'&selectType='+selecttype)
content = html.read().decode('utf-8')

jcontent = json.loads(content)
data = jcontent['data']

data=[ i for i in data if i[4]!='-']

# 此次用升冪(預設),故不特別定義reverse
Dividend_list = sorted(data,key=lambda x:float(x[5].replace(',','')))[:100]
print(Dividend_list)