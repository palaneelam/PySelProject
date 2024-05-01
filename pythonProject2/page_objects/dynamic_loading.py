from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext
from object_repository.or_add_remove_page import dynamic_loading_homepage


def test_dynamiclanding_homepage(driver):

    elem1 = wait_for_visibility_of_element_linktext(driver,dynamic_loading_homepage)
    elem1.click()