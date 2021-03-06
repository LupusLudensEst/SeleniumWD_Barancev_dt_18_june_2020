# [x] Задание 19. Реализовать многослойную архитектуру
# Переделайте созданный в задании 13 сценарий для добавления товаров в корзину и удаления товаров из корзины, чтобы он использовал многослойную архитектуру.
#
# А именно, выделите вспомогательные классы для работы с главной страницей (откуда выбирается товар), для работы со страницей товара (откуда происходит добавление товара в корзину), со страницей корзины (откуда происходит удаление), и реализуйте сценарий, который не напрямую обращается к операциям Selenium, а оперирует вышеперечисленными объектами-страницами.
#
# -----
#
# Уложите созданные файлы в ранее созданный репозиторий. В качестве ответа на задание отправьте ссылку на свой репозиторий и указание, где лежат нужные файлы.
#
# Submission status
# Attempt number	This is attempt 1.
# Submission status	Submitted for grading
# Grading status	Graded
# Last modified	Tuesday, 28 July 2020, 11:25 PM
# Online text
# View summary
# Good evening, boss.
#
# Find herein hw_19: https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/features/tests/pop_bdd_hw_19.feature
# The layers of architecture:
#
# 1. pages: base_page.py (methods and login), main_page(execution of the add/delete items to bin)-correlates with this very homework;
#
# 2. app: application (connecting class from low level to high level layers);
#
# 3. features: tests (. feature=Gerking files=scenarios of high level), steps (.py=subdue of Gerking files for transmitting commands to lower level);
#
# 5. environment.py;
#
# 6. See folder READ_ME: with manual for Allure reporting system and attached screenshot.
#
# Sincerely, Vic
#
# to_hw19_dt_28_july_2020
#
#
#
# Make changes to your submission
# Feedback
# Grade	сдано!
# Graded on	Wednesday, 29 July 2020, 2:20 AM
# Graded by	Picture of Алексей БаранцевАлексей Баранцев
# Feedback comments
# Верно.

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Different drivers
@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
    # wd = webdriver.Firefox()
    # options = webdriver.FirefoxOptions()
    # options.binary_location = "C:\\Program Files\\Firefox Nightly\\firefox.exe"
    # options.add_argument("start-maximized")
    # wd = webdriver.Firefox(firefox_options=options)
    # new method
    # wd = webdriver.Firefox()
    # new method more obviously
    # wd = webdriver.Firefox(capabilities={"marionette": True})
    # old method
    # wd = webdriver.Firefox(capabilities={"marionette": False})
    # wd = webdriver.Edge(executable_path="C:\Webdrivers\msedgedriver")
    # wd = webdriver.Ie()
    # wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    # wd = webdriver.Ie(capabilities={"IntroduceInstabilityByIgnoringProtectedModeSettings": True, "requireWindowFocus": True, "unexpectedAlertBehaviour": "dismiss", "ignoreZoomSetting": True})
    # print(f'\nCAPABILITIES: {wd.capabilities}\nEND CAPABILITIES')
    print(f'\nWD capabilities: {wd.capabilities}\n')
    request.addfinalizer(wd.quit)
    return wd

# Go to the product page
def test_cart(driver):
    driver.get("https://litecart.stqa.ru/en/")
    driver.maximize_window()

# Quantity of the items defined
    add_to_cart(driver, 3)
    del_from_cart(driver)

# Add to cart
def add_to_cart(driver, count = 1):
    wait = WebDriverWait(driver, 10)
    for i in range(count):
        # Click on first item in the list
        aa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#box-most-popular a")))
        aa.click()
        # In case item has a select option
        box_product = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#box-product")))[0]
        selectors = box_product.find_elements(By.CSS_SELECTOR, "select[name='options[Size]']")
        if (len(selectors) > 0):
            Select(selectors[0]).select_by_index(1)
        # Click on Add To Cart button
        bb = wait.until(EC.element_to_be_clickable((By.NAME, "add_cart_product")))
        bb.click()
        # Waiting new quantity counter in the cart
        counter = int(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.quantity"))).text)
        WebDriverWait(driver, 10).until(lambda s: int(s.find_element(By.CSS_SELECTOR, "span.quantity").text) == counter + 1)
        print(f'\n        Items in the cart: {counter + 1}')
        # Step back in the browser hystory
        driver.back()

# Delete from cart
def del_from_cart(driver):
    wait = WebDriverWait(driver, 10)
    # Click on checkout
    cc = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#cart a.link")))
    cc.click()
    # Iterate delete till table with items is not empthy
    counter = len(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.dataTable tr"))).text)
    while counter > 0:
        dd = wait.until(EC.element_to_be_clickable((By.NAME, "remove_cart_item")))
        dd.click()
        WebDriverWait(driver, 10).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, "table.dataTable tr")) < counter)
        counter = len(driver.find_elements(By.CSS_SELECTOR, "table.dataTable tr"))
        print(f'\nRows in the table after deleting one more item: {counter}')
    # Step back in the browser hystory
    driver.back()

# # Verify page has a text 'Invalid Login'
# def text_here(driver):
#     wait = WebDriverWait(driver, 10)
#     cc = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#checkout-cart-wrapper")))
#     actual_text = cc.text
#     assert 'There are no items in your cart.5' in actual_text
#     print(f'Text is here: "{actual_text}" ')
#     # Step back in the browser hystory
#     driver.back()