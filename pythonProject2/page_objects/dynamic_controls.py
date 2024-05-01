from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext
from object_repository.or_add_remove_page import dynamic_controls_homepage


def test_dynamiccontrols_homepage(driver):

    elem1 = wait_for_visibility_of_element_linktext(driver,dynamic_controls_homepage)
    elem1.click()