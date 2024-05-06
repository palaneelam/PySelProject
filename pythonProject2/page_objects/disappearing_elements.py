from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext
from object_repository.or_add_remove_page import disappearing_elements


def test_disappearingelement_homepage(driver):

    elem1 = wait_for_visibility_of_element_linktext(driver,disappearing_elements)
    elem1.click()