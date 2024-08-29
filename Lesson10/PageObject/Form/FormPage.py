from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, browser)->None:
        self.browser = browser
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        self.browser.implicitly_wait(4)
        self.browser.maximize_window()


    def open(self)->None:
        self.browser.get(self.url)


    def fill_fields(self, v_dict)->None:
        for k in v_dict:
            selector = f'[name={k}]'
            value = v_dict[k]
            self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(value)


    def click_submit(self)->str:
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    
    def find_element_property(self, locator)->list[str]:
        background_color = self.browser.find_element(By.ID, locator).value_of_css_property("background-color")
        return background_color