import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

EMAIL = 'Your e-mail address' 
PASSWORD = 'Your password'
CHROMEDRIVER_PATH = '/paht/to/chromedriver'

options = Options()
options.add_argument('-headless')
options.add_argument('--no-sandox')
options.add_argument('--disable-setuid-sandbox')


driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
driver.get('https://sakito.cirkit.jp/user/sign_in')

# ログイン
email_input = driver.find_element_by_id('user_email')
email_input.send_keys(EMAIL)
password_input = driver.find_element_by_id('user_password')
password_input.send_keys(PASSWORD)
login_btn = driver.find_element_by_css_selector('#new_user > input.btn.btn-info.btn-block')
login_btn.click()

# ポイントガチャを回す
driver.get('https://sakito.cirkit.jp/user/point/new')
gatya_btn = driver.find_element_by_css_selector('body > div > div > div > div > a')
gatya_btn.click()

# 終了
driver.quit()