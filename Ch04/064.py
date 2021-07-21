# 從 yahoo取得當日熱門股

from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

type = sys.argv[1]

html = urlopen('https://tw.stock.yahoo.com/d/i/rank.php?t='+type+'&e=tse&n=50')

soup = BeautifulSoup(html, 'html.parser')

for i in soup.find_all('div', class_='Lh(20px) Fw(600) Fz(16px) Ell'):
    print(i.contents)

# 參數名稱已變
# python 064.py volume
# html 結構已變
# <div class="Lh(20px) Fw(600) Fz(16px) Ell">長榮</div>
# <div class="Lh(20px) Fw(600) Fz(16px) Ell">陽明</div>

# Fz(14px) C(#979ba7) Ell
# Fz(14px) C(#979ba7) Ell