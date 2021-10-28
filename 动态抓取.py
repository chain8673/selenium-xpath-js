from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素

url = 'http://vip.win007.com/AsianOdds_n.aspx?id=2038440&l=0'

# 将浏览器隐藏
option = webdriver.ChromeOptions()
option.add_argument('headless')  # 设置option
browser = webdriver.Chrome(options=option)

browser.get(url)
wait = WebDriverWait(browser, 10) #验证10秒之内，browser是否执行完成
wait.until(EC.presence_of_element_located((By.ID, 'odds'))) #等等ID为odds的元素出现

tag = browser.find_element(By.XPATH, '//*[@id="odds"]/tbody/tr[3]/td[12]/a[1]')
print(tag.get_attribute('href'))
