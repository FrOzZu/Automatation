import allure
from selenium.webdriver.common.by import By

class AuthorizationPage: 
    

    def __init__(self, driver) ->None:
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Авторизация пользователя {name}:{password}")   
    def auth(self, name: str, password: str)-> None:
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()