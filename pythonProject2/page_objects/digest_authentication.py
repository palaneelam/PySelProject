from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext
from object_repository.or_add_remove_page import digest_auth_homepage


def test_dynamicauth_homepage(driver):

    elem1 = wait_for_visibility_of_element_linktext(driver,digest_auth_homepage)
    elem1.click()

