import pytest
from selenium import webdriver

from Shop.AuthorizationPage import AuthorizationPage
from Shop.MainPage import MainPage
from Shop.CartPage import CartPage


@pytest.mark.test_shop
def test_price():
    browser = webdriver.Chrome()
    auth = AuthorizationPage(browser)
    auth.auth("standard_user", "secret_sauce")
    
    main_p = MainPage(browser)
    main_p.add_items()
    
    cart = CartPage(browser)
    cart.get_cart()
    cart.send_data("Evgenii", "Gainulin", 620000)
    as_is = (cart.total_price())
    to_be = "Total: $58.29"
    assert as_is == to_be
    browser.quit()