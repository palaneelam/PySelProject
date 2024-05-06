
from config.test_setting import TestSettings
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




def wait_for_visibility_of_element_xpath(driver, xpathValue):
    try:
        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, xpathValue)))
    except Exception as e:
        print("Timeout exception:", e)
    return element

def wait_for_visibility_of_element_linktext(driver,lintextvalue):
    try:
        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,lintextvalue)))
    except Exception as e:
        print("Timeout exception:", e)
    return element

def wait_for_visibility_of_element_tagname(driver,tagname):
    try:
        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.TAG_NAME,tagname)))
    except Exception as e:
        print("Timeout exception:", e)
    return element

# def wait_for_visibility_of_element_id(driver,id):
#     try:
#         element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.TAG_NAME,id)))
#     except Exception as e:
#         print("Timeout exception:", e)
#     return element
def goto_Homepage(driver):
    driver.get(TestSettings.page_url)









