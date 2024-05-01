from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext
from object_repository.or_add_remove_page import exit_intent_homepage


def test_exitintent_homepage(driver):

    elem1 = wait_for_visibility_of_element_linktext(driver,exit_intent_homepage)
    elem1.click()