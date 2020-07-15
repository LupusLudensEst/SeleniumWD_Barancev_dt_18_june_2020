import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from random import randint
import os
import datetime

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

    # Log in to URL: http://localhost/litecart/admin/
def test_litecart(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.maximize_window()
    sleep(2)

    # Enter login: admin
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("admin")

    # Enter password: admin
    driver.find_element(By.NAME,"password").clear()
    driver.find_element(By.NAME,"password").send_keys("admin")

    # Click Login button
    driver.find_element(By.NAME,"login").click()
    sleep(2)

    # Click Catalog button
    driver.find_element(By.XPATH, "//span[contains(text(), 'Catalog')]").click()
    sleep(2)

    # Click Add New Product button
    add_product_btn = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.button")))
    add_product_btn[1].click()
    sleep(2)

    # Click on General folder
    driver.find_element(By.XPATH, "//a[contains(text(), 'General')]").click()
    sleep(2)

    # Click on Enabled radio button
    if not driver.find_element(By.NAME, "status").is_selected():
        driver.find_element(By.NAME, "status").click()

    # Fill out Name field
    driver.find_element(By.NAME, "name[en]").clear()
    driver.find_element(By.NAME,"name[en]").send_keys("Abirvalg")

    # Fill out Code field
    driver.find_element(By.NAME, "code").clear()
    driver.find_element(By.NAME,"code").send_keys("428958")

    # Check on Unisex checkbox
    driver.find_element(By.XPATH, "//input[@value='1-3']").click()

    # Fill out Quantity field
    driver.find_element(By.XPATH, "//input[@name='quantity']").clear()
    driver.find_element(By.XPATH,"//input[@name='quantity']").send_keys("1")

    # Fill out Quantity Unit field
    quantity = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "quantity_unit_id")))
    quantity.click()
    selector = Select(quantity)
    selector.select_by_visible_text('pcs')
    print(f'\nQuantity: {quantity}; Selector: {selector}\n')

    # Fill out Delivery Status field
    delivery = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "delivery_status_id")))
    delivery.click()
    selector = Select(delivery)
    selector.select_by_visible_text('3-5 days')
    print(f'\nDelivery Status: {delivery}; Selector: {selector}\n')

    # Fill out Sold Out Status field
    sold_out = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "sold_out_status_id")))
    sold_out.click()
    selector = Select(sold_out)
    selector.select_by_visible_text('Temporary sold out')
    print(f'\nSold Out Status: {sold_out}; Selector: {selector}\n')

    # Upload a pic by clicking on Choose File button
    product_image = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'Guessed_baby_face.png'))
    driver.find_element(By.NAME, "new_images[]").send_keys(product_image)
    print(f'\nProduct image: {product_image}')

    # # Set data Date Valid From
    date_from = datetime.date.today()
    driver.find_element(By.NAME, "date_valid_from").send_keys(date_from.strftime('%m-%d-%Y'))
    date_to = datetime.date.today() + datetime.timedelta(days=15)
    driver.find_element(By.NAME, "date_valid_to").send_keys(date_to.strftime('%m-%d-%Y'))

    # Click on Information folder
    driver.find_element(By.CSS_SELECTOR, "[href='#tab-information']").click()

    # Select Manufacturer from drop down menu
    manufacturer = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "manufacturer_id")))
    manufacturer.click()
    selector = Select(manufacturer)
    selector.select_by_visible_text('ACME Corp.')
    print(f'\nManufacturer: {manufacturer}; Selector: {selector}\n')

    # Fill out Keywords field
    driver.find_element(By.NAME, "keywords").clear()
    driver.find_element(By.NAME,"keywords").send_keys("Abirvalg")

    # Fill out Short Description field
    driver.find_element(By.NAME, "short_description[en]").clear()
    driver.find_element(By.NAME,"short_description[en]").send_keys("Abirvalg-is what Sharikov said in Dog's heart")

    # Fill out Description field
    driver.find_element(By.CSS_SELECTOR, "div.trumbowyg-editor").clear()
    driver.find_element(By.CSS_SELECTOR, "div.trumbowyg-editor").send_keys("Abirvalg-is what Sharikov said in Dog's heart by M.A. Bulgakov")

    # Fill out Head Title field
    driver.find_element(By.NAME, "head_title[en]").clear()
    driver.find_element(By.NAME,"head_title[en]").send_keys("Avirvalg != Gravriba")

    # Fill out Meta Description field
    driver.find_element(By.NAME, "meta_description[en]").clear()
    driver.find_element(By.NAME,"meta_description[en]").send_keys("Avirvalg != Gravriba. Metadescription")

    # Click on Prices folder
    driver.find_element(By.CSS_SELECTOR, "[href='#tab-prices']").click()

    # Fill out Purchase Price field
    driver.find_element(By.NAME, "purchase_price").clear()
    driver.find_element(By.NAME, "purchase_price").send_keys("999999")

    # Select Currency from drop down menu
    currency = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "purchase_price_currency_code")))
    currency.click()
    selector = Select(currency)
    selector.select_by_visible_text('US Dollars')
    print(f'\nCurrency: {currency}; Selector: {selector}\n')

    # Select Tax Class from drop down menu
    tax_class = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "tax_class_id")))
    tax_class.click()
    selector = Select(tax_class)
    selector.select_by_visible_text('Standard')
    print(f'\nTax Class: {tax_class}; Selector: {selector}\n')

    # Fill out Price Incl. Tax (?) USD field
    driver.find_element(By.NAME, "gross_prices[USD]").clear()
    driver.find_element(By.NAME, "gross_prices[USD]").send_keys("999")

    # Fill out Price Incl. Tax (?) EURO field
    driver.find_element(By.NAME, "gross_prices[EUR]").clear()
    driver.find_element(By.NAME, "gross_prices[EUR]").send_keys("9999")

    # Click on Save button save
    driver.find_element(By.NAME, "save").click()

    # Verify Abirvalg as a new good is here in Catalog
    xpath_avirvalg = './/a[contains(.,\'' + "Abirvalg" + '\')]'
    print(xpath_avirvalg)
    catalog = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "form[name=catalog_form")))[0]
    catalog.find_element(By.XPATH, xpath_avirvalg).click()