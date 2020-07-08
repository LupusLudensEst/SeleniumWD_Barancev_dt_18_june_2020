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
driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
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

# # Countries table/ct
# # ct = driver.find_elements(By.CSS_SELECTOR, "tr.row")
# ct = driver.find_elements(By.XPATH, "//tr[@class='row']")
# len_ct = len(ct)
# print(f'Lenght of table: {len_ct}\n')
# # Looking for something/st
# st = driver.find_elements(By.XPATH, ".//*[@id='table-zones']//tr [not(contains (@class, 'header'))]")
# len_st = len(st)

# rows=driver.find_elements(By.XPATH, ".//tr[@class='row']")
rows=driver.find_elements(By.XPATH, ".//*[@id='table-zones']//tr [not(contains (@class, 'header'))]")
print ('Length of something: '+str(len(rows)) + '\n')
column_z = driver.find_elements(By.TAG_NAME, "td")

# Extracting data from coulumn #3(index 2)
zones_name = []
for elements in rows:
    column_z = elements.find_elements(By.TAG_NAME, "td")
    zones_name.append(column_z[2].text)
print(f'Column Z: {column_z[2].text}\n')
# It deletes and returns the last element from list with index i list.pop([i]), becuse it is the filter field
# by default deleted the last element
# Nothing to delete from empty list
# zones_name.pop()
sorted_zones_list = sorted(zones_name)
print(f'Zones name: {zones_name}\nSorted zone names: {sorted_zones_list}\n')
assert zones_name == sorted_zones_list
print(f'Text of zones name: {str(zones_name.append(column_z[2].text))}\n')

# Get into every from the countries and verify that zones are in the alphabet order
driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
# Get into every from the countries
geozones_list_text = []
# Set of links for countries with the zones
geo_links = driver.find_elements_by_xpath(
    ".//*[@id='content']/form/table/tbody/tr[@class='row']/td [not(contains (@style,'text'))]/a")
for link in geo_links:
    print(f'Link get attribute: {link.get_attribute("href")}\n')
    geozones_list_text.append(link.get_attribute('href'))
# Append links into special array to prevent Selenium from
# errors like this python Message: stale element reference: element is not attached to the page document

# Run through the lists in the opened pages
for i in range(len(geozones_list_text)):
    geozones_list = []  # Nullifying the list
    driver.get(geozones_list_text[i])
    geo_zones_in_selects = driver.find_elements_by_xpath(
        ".//*[@id='table-zones']/tbody/tr/td/select[starts-with(@name,'zones[') and not(contains (@aria-hidden,'true'))]/option[@selected='selected']")
    for geozones in geo_zones_in_selects:
        geozones_list.append(geozones.text)

    sorted_geozones_list = sorted(geozones_list)
    print(f'Geo zones list: {geozones_list}\n')
    assert geozones_list == sorted_geozones_list

# txt_ct = driver.find_elements(By.CSS_SELECTOR, "tr.row").text
# print(f'Text1: {txt_ct}\n')

# # Looking for column Name/cn
# cn = driver.find_elements(By.XPATH, "//*[@id='content']/form/table/tbody/tr[1]/th[5]")
# len_cn = len(cn)
# txt_cn = driver.find_element(By.XPATH, "//*[@id='content']/form/table/tbody/tr[1]/th[5]").text
# print(f'Lenght2: {len_cn}')
# print(f'Text2: {txt_cn}\n')
#
# # Looking for Zone/zn
# driver.get('http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=US')
# sleep(2)
# zn = driver.find_elements(By.XPATH, ".//*[@id='table-zones']//tr [not(contains (@class, 'header'))]")
# len_zn = len(cn)
# txt_zn = driver.find_element(By.XPATH, ".//*[@id='table-zones']//tr [not(contains (@class, 'header'))]").text
# print(f'Lenght3: {len_zn}')
# print(f'Text3: {txt_zn}\n')

driver.quit()