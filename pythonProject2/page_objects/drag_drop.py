from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext
from object_repository.or_add_remove_page import drag_drop_homepae


def test_dragdrop_homepage(driver):

    elem1 = wait_for_visibility_of_element_linktext(driver,drag_drop_homepae)
    elem1.click()