from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext, \
    wait_for_visibility_of_element_xpath
from object_repository.or_add_remove_page import checkbox_homepage, secondchckbox


def test_checkbox_homepage(driver):
    elem1 = wait_for_visibility_of_element_linktext(driver,checkbox_homepage)
    elem1.click()

def test_secondcheckbox(driver):
    chckbox2= wait_for_visibility_of_element_xpath(driver,secondchckbox)
    chckbox2.click()
