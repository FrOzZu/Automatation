import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver,5)

driver.get("https://www.saucedemo.com/")
login = driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="app_logo"]'), "Swag Labs")
)

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="app_logo"]'), "Swag Labs")
)
first_n = driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Anastasia")
last_n = driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Kuzko")
zipcode = driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("236040")
driver.find_element(By.CSS_SELECTOR, "#continue").click()
waiter.until(
    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="header_container"]/div[2]/span'), "Checkout: Overview")
)


@pytest.mark.test_shop
@pytest.mark.parametrize('res_in, res_es', [
        (driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').get_attribute("textContent"), 'Total: $58.29')
        ])
def test_price (res_in, res_es):
    assert res_in == res_es
    if res_in == res_es:
        print("success")
    else:
        print("false")  

driver.quit()