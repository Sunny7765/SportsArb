from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(executable_path='/home/sunny/Flashpoint/FPSoftware/Chromium/chromedriver', options=options)
driver.get("https://www.google.com")
print(driver.title)

driver.quit()