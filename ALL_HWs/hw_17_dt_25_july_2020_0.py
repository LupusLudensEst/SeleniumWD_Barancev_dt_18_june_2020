# hw17 dt 25 july 2020
# Протоколирование действий Selenium
# EventFiringWebDriver: Python

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from datetime import date
from random import randint

# Generator of random integer
ran_int = str(randint(999, 9999))

# Generator of current day
today = date.today()
screen_png = str(today) + '_' + ran_int + '_screen.png'

class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)
    def after_find(self, by, value, driver):
        print(by, value, "Element found")
    def on_exception(self, exception, driver):
        # Snippet below is for screenshot
        screen_path = str("C:\\Everything\\IT\\Testing\\Automation_08_09_2019\\SeleniumWD_Barancev_dt_18_june_2020\\\Screens\\" + screen_png)
        driver.get_screenshot_as_file(screen_path)
        print(f'Exception-{exception}')

@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()
    wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    # wd = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
    # wd = webdriver.Firefox()
    # wd = EventFiringWebDriver(webdriver.Firefox(), MyListener())
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
    # wd = EventFiringWebDriver(webdriver.Edge(executable_path="C:\Webdrivers\msedgedriver"), MyListener())
    # wd = webdriver.Ie()
    # wd = EventFiringWebDriver(webdriver.Ie(), MyListener())
    # wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    # wd = webdriver.Ie(capabilities={"IntroduceInstabilityByIgnoringProtectedModeSettings": True, "requireWindowFocus": True, "unexpectedAlertBehaviour": "dismiss", "ignoreZoomSetting": True})
    # print(f'\nCAPABILITIES: {wd.capabilities}\nEND CAPABILITIES')
    print(f'WD capabilities: {wd.capabilities}\n')
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    # pass
    driver.get("https://www.google.com/")
    driver.maximize_window()
    for l in driver.get_log("browser"):
        print(f'Browser log: {l}')
    sleep(2)
    driver.find_element(By.NAME, "q").clear()
    sleep(2)
    driver.find_element(By.NAME, "q").send_keys("webdriver")
    sleep(2)
    driver.find_element(By.NAME, "_btnK").click() # Correct is: "btnK"
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Google Search"))
    print("Browser log: " + str(driver.get_log("browser")))
    print("Driver log: " + str(driver.get_log("driver")))




