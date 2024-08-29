import allure
import pytest
from selenium import webdriver

from Authorization_Page import AuthorizationPage
from Main_Page import MainPage
from Cart_Page import CartPage

@allure.title("Поверка итоговой суммы в магазине")
@allure.description("Тест, который сравнивает сумму добавленную в корзину с конкретным значением")
@allure.feature("CREATE")
@allure.severity("blocker")

@pytest.mark.test_shop
def test_price():
    with allure.step("Запуск браузера Chorme"):
     browser = webdriver.Chrome()

    with allure.step("Авторизация"):
     auth = AuthorizationPage(browser)
     auth.auth("standard_user", "secret_sauce")
    
    with allure.step("Добавление товаров в корзину"):
     main_p = MainPage(browser)
     main_p.add_items()

    with allure.step("Переход в корзину"):
     cart = CartPage(browser)
     cart.get_cart()

    with allure.step("Ввод персональных данных"):
     cart.send_data("Evgenii", "Gainulin", 620000)
    as_is = (cart.total_price())

    with allure.step("Сравнение итоговой стоимости с конкретным значением"):
     to_be = 'Total: $58.29'
    assert as_is == to_be
    
    browser.quit()