# [x] Задание 7. Сделайте сценарий, проходящий по всем разделам админки
# Сделайте сценарий, который выполняет следующие действия в учебном приложении litecart.
#
# 1) входит в панель администратора http://localhost/litecart/admin
# 2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
# 3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
#
# Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.
#
# Если возникают проблемы с выбором локаторов для поиска элементов -- обращайтесь в чат за помощью.
#
# -----
#
# Уложите созданный файл, содержащий сценарий, в ранее созданный репозиторий. В качестве ответа на задание отправьте ссылку на свой репозиторий и указание, какой именно файл содержит нужный сценарий.
#
# Submission status
# Attempt number	This is attempt 4.
# Submission status	Submitted for grading
# Grading status	Graded
# Last modified	Saturday, 4 July 2020, 10:51 PM
# Online text
# View summary
# Hello, boss.
#
# One more attempt. Hope last one.
#
# https://github.com/LupusLudensEst/SeleniumWD_Barancev_dt_18_june_2020/blob/master/homework_dt_02_july_2020_2.py
#
# Sincerely, Vic

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture
def wd(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

# Init driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the url
driver.get('http://localhost/litecart/admin/')
sleep(2)

#Input into the field "Username"
search = driver.find_element(By.NAME, "username")
search.clear()
search.send_keys('admin')
sleep(1)

#Input into the field "Password"
search = driver.find_element(By.NAME, "password")
search.clear()
search.send_keys('admin')
sleep(1)

#Click on button "Login"
driver.find_element(By.NAME, 'login').click()
sleep(2)

link_array = []
h1_array = []
# Main menu/mm
mm = driver.find_elements(By.XPATH, "//*[@id='app-']/a/span[2]")
for i in range(len(mm)):
    mm_el = driver.find_elements(By.XPATH, "//*[@id='app-']/a/span[2]")
# Name of main menu item
    link_name = mm_el[i].text
    print('#:' + str(i) + "." + link_name + ';')
# Main menu element/mm_l
    mm_el[i].click()
    driver.implicitly_wait(1)
    sub_menu = driver.find_elements(By.XPATH, "//ul[@class='docs']//li//span")
    print("   Total submenu elements:" + str(len(sub_menu)))
# If no submenu
    if len(sub_menu) < 1:
        head_title = driver.find_element(By.XPATH, ".//*[@id='content']/h1").text
        print("     Main Link_text  : " + link_name + ";")
        print("     Head_title : " + head_title + ";")
        link_array.append(link_name)
        h1_array.append(head_title)
# If submenu
    for j in range(len(sub_menu)):
        sub_menu_el = driver.find_elements(By.XPATH, "//ul[@class='docs']//li//span")
        sub_menu_el[j].click()
        # rereading after click and looking for h1
        sub_menu_el = driver.find_elements(By.XPATH, "//ul[@class='docs']//li//span")
        sub_m_link_name = sub_menu_el[j].text
        head_title2 = driver.find_element(By.XPATH, ".//*[@id='content']/h1").text

        print("     Link_text  : " + sub_m_link_name)
        print("     Head_title : " + head_title2)
        link_array.append(sub_m_link_name)
        h1_array.append(head_title2)

        print('Total: ' + str(len(link_array)) + ' links.')
        print(link_array)
        print('Total: ' + str(len(h1_array)) + ' head titles with h1.')
        print(h1_array)
    assert len(link_array) == len(h1_array)

driver.quit()