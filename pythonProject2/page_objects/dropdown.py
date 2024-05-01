from select import select
from selenium.webdriver.support.select import Select

from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext, \
    wait_for_visibility_of_element_xpath
from object_repository.or_add_remove_page import dropdown_homepage, dropdownid


def test_dropdown_homepage(driver):

    elem1 = wait_for_visibility_of_element_linktext(driver,dropdown_homepage)
    elem1.click()

def test_select_dropdownValue(driver):
    dropdown=Select(wait_for_visibility_of_element_xpath(driver,dropdownid))
    dropdown.select_by_index(2)
