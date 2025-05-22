# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from fake_useragent import UserAgent
# import undetected_chromedriver as uc
# import time

# try:
#     options = Options()
#     ua = UserAgent()
#     user_agent = ua.random
#     print(user_agent)
#     options.add_argument(f'user-agent={user_agent}')
#     driver = uc.Chrome(options=options)
#     driver.get(url='https://www.list.am/')
#     driver.maximize_window()
#     time.sleep(4)
#     driver.find_element(By.CSS_SELECTOR, '#dlgLangSel > div.bar > a:nth-child(1)').click()
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#hcontent > div.stripc > div:nth-child(2) > a').click()
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#main > div.catms > div > div:nth-child(2) > a').click()
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#main > div.catms > div > div:nth-child(1) > a').click()
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(4) > div > div.co4 > div.me > img').click()
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(4) > div > div.co4 > div.l.top > div:nth-child(13)').click()
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#idprice1').send_keys('20000')
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#idprice2').send_keys('25000')
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div > div.me > img').click()
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div > div.l.top > div:nth-child(2)').click()
#     time.sleep(1)
#     with open('cars.txt', 'a', encoding='utf-8') as file:
#         for i in range(1, 97):
#             car = driver.find_element(By.CSS_SELECTOR, f'#contentr > div.dl > div.gl > a:nth-child({i})')
#             file.write(f'{car.text}\n')
# except Exception as ex:
#     print(ex.__class__.__name__)