### 060 產業別股票清單

from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

id = sys.argv[1]

html = urlopen('https://www.moneydj.com/z/zh/zha/ZH00.djhtm?A='+id)
soup =BeautifulSoup(html,'html.parser')

for i in soup.find_all('td',id='oAddCheckbox'):
    print(i.find('a').contents)

# <td nowrap="" id="oAddCheckbox" class="t3t1">
# <a href="javascript:Link2Stk('AS1101');">1101台泥</a></td>

print (soup)