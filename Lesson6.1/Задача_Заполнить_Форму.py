import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver

def test_fill_and_submit_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

                                  # Заполнение формы 
    driver.find_element(By.CSS_SELECTOR, "input[name=first-name]").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name=last-name]").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name=address").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name=e-mail]").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name=phone]").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name=zip-code]").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "input[name=city]").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name=country]").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name=job-position]").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name=company]").send_keys("SkyPro")

                                   # Нажатие кнопки Submit

    submit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button) 
    driver.execute_script("arguments[0].click();", submit_button)

                                   # Ожидание подсветки полей

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "main[class=flex-shrink-2]"))
    )

                                   # Проверка, что поле Zip code подсвечено красным

    zip_code_field = driver.find_element(By.CSS_SELECTOR, "div#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

                                   # Проверка, что остальные поля подсвечены зеленым

    green_highlighted_fields = driver.find_elements(By.CSS_SELECTOR, "div.alert.py-2.alert-success")
    assert len(green_highlighted_fields) == 9  # Должно быть 9 успешно подсвеченных полей
                                  
                                   # Проверка, что поле Zip code подсвечено красным

    zip_code_field = driver.find_element(By.CSS_SELECTOR, "div#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

                                  # Проверка, что остальные поля подсвечены зеленым

    green_highlighted_fields = driver.find_elements(By.CSS_SELECTOR, "div.alert.py-2.alert-success")
    assert len(green_highlighted_fields) == 9  # Должно быть 9 успешно подсвеченных полей

if __name__ == "__main__":
    pytest.main()