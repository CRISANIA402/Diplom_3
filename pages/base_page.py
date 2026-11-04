import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seletools.actions import drag_and_drop as drag_and_drop_action


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открываем страницу по адресу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ждём видимый элемент и возвращаем его")
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ждём элемент в DOM и возвращаем его")
    def find_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Ждём элементы в DOM и возвращаем их список")
    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликаем по элементу")
    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except ElementClickInterceptedException:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Перетаскиваем элемент в целевую зону")
    def drag_and_drop(self, source, target):
        """Selenium-драйвер не порождает HTML5 drag-события,
        поэтому используется seletools. Драйвер используется
        только в базовом классе."""
        drag_and_drop_action(self.driver, source, target)

    @allure.step("Ждём невидимости элемента")
    def wait_for_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Получаем текст элемента")
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step("Получаем текущий адрес страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ждём адрес страницы {url}")
    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))
