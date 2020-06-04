import time
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_find_buy_basket(browser):

    browser.get(link)
    time.sleep(10)
    buy_box = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert buy_box, print('ERROR')