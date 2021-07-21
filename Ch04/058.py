# 058

# pip install selenium

# chrome webdriver
# http://chromedriver.chromium.org/downloads

from selenium import webdriver
web = webdriver.Chrome('chromedriver.exe')


# 無圖形介面操作
option = webdriver.ChromeOptions()
option.add_argument('headless')
web = webdriver.Chrome('chromedriver.exe', chrome_options=option)
