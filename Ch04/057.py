### 安裝 BeautifulSoup

# pip install bs4

from bs4 import BeautifulSoup

res = open('websample.html',encoding='utf8').read()
print(res)

soup = BeautifulSoup(open('websample.html',encoding='utf8'))
print(soup)

p = soup.find('p')
ap = soup.find_all('p')

print(p)
print(ap)