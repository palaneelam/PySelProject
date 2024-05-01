from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext
from object_repository.or_add_remove_page import basicauthbtn, brknimg_homepage


def test_brokenimg_homepage(driver):
    elem1 = wait_for_visibility_of_element_linktext(driver,brknimg_homepage)
    elem1.click()