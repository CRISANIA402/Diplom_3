from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        """Ждёт видимый элемент и возвращает его."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_present(self, locator):
        """Ждёт элемент в DOM (даже если он невидимый)."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        """Ждёт элементы в DOM и возвращает список найденных."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Ждёт кликабельности элемента и кликает по нему.
        Если клик перехватил оверлей модалки (флейка Firefox на стенде),
        повторяет клик через JS — он не зависит от перекрытий."""
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except ElementClickInterceptedException:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        return self.find(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))
