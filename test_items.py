import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button_existed(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    basket = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    print('\n', basket.text)
    assert basket != None, "the button is missing"
    time.sleep(30)
