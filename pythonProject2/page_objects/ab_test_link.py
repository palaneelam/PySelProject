from FunctionLibraries.common_methods import wait_for_visibility_of_element_xpath, \
    wait_for_visibility_of_element_linktext
from object_repository.or_add_remove_page import ab_testing_homepage


def click_AB_testing(driver):
    elem1= wait_for_visibility_of_element_linktext(driver,ab_testing_homepage)
    elem1.click()