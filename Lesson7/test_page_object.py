import pytest
from selenium import webdriver

from PageObject.Main_Page import Main_Page 
from PageObject.Result_PAGE import Result_PAGE
from PageObject.Cart_Page import Cart_Page

@pytest.mark.test_labirint   
def test_cart_counter():
    browser = webdriver.Chrome()
    main_page = Main_Page(browser)
    main_page.set_cookie_policy()
    main_page.serch("Python")
   
    result_page = Result_PAGE(browser)
    to_be = result_page.add_books()
    
    cart_page = Cart_Page(browser)
    cart_page.get()
    as_is = cart_page.get_counter() 

    assert as_is == to_be
    browser.quit()
   

@pytest.mark.test_labirint  
def test_empty_search():
    browser = webdriver.Chrome() 
    main_page = Main_Page(browser) 
    main_page.set_cookie_policy()
    main_page.serch("no book search term")

    result_page = Result_PAGE(browser)
    msg = result_page.get_empty_result_message()
    assert msg == "Мы ничего не нашли по вашему запросу! Что делать?"
    browser.quit()