from FunctionLibraries.common_methods import wait_for_visibility_of_element_xpath
from object_repository.or_add_remove_page import add_remove_link_home_page, ab_testing_homepage


def click_add_remove_link(driver):
    elem = wait_for_visibility_of_element_xpath(driver, add_remove_link_home_page)
    # elem = driver.find_element(By.XPATH, add_remove_link_home_page)
    elem.click()

