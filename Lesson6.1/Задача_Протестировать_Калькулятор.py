import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver,47)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
delay = driver.find_element(By.CSS_SELECTOR, "#delay")
delay.clear()
delay.send_keys("45")
driver.find_element(By.XPATH, "//span[contains(text(),'7')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'8')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[class='screen']"), "15")
)

@pytest.mark.test_calculator
@pytest.mark.parametrize('res_in, res_es', [
        (driver.find_element(By.CSS_SELECTOR, "div[class='screen']").get_attribute("innerText"), '15')
        ])
def test_sum(res_in, res_es):
    assert res_es == res_in

driver.quit()