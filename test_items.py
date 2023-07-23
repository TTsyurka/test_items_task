import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    basket = browser.find_element(By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs > span > a')
    print(basket.text)
    time.sleep(15)
