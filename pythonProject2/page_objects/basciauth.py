from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext
from object_repository.or_add_remove_page import basicauthbtn


def test_basicauth(driver):
    elem1 = wait_for_visibility_of_element_linktext (driver,basicauthbtn )
    elem1.click()