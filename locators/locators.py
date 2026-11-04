from selenium.webdriver.common.by import By


class Locators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//div[contains(@class,'BurgerIngredient')]"
        "[.//img[@alt='Флюоресцентная булка R2-D3']]"
        "//p[contains(@class,'counter')]",
    )

    CONSTRUCTOR_AREA = (
        By.XPATH,
        "//span[contains(text(),'булочку сюда')]"
        "/ancestor::div[contains(@class,'constructor-element')]",
    )

    INGREDIENT_MODAL_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    TOTAL_DONE_COUNTER = (
        By.XPATH,
        "//p[contains(text(),'Выполнено за все время')]/following-sibling::p",
    )
    TODAY_DONE_COUNTER = (
        By.XPATH,
        "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p",
    )

    IN_WORK_NUMBERS = (
        By.XPATH,
        "//p[text()='В работе:']/following-sibling::ul/li",
    )
    
    INGREDIENT_CARD = (
        By.XPATH,
        "//div[contains(@class,'BurgerIngredient')]"
        "[.//img[@alt='Флюоресцентная булка R2-D3']]",
    )
