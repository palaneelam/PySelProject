from FunctionLibraries.common_methods import wait_for_visibility_of_element_linktext, \
    wait_for_visibility_of_element_tagname
from object_repository.or_add_remove_page import context_menu_homepage, context_title


def test_contextmenu_homepage(driver):

    elem1 = wait_for_visibility_of_element_linktext(driver,context_menu_homepage)
    elem1.click()

def test_context_title(driver):
    elem2=wait_for_visibility_of_element_tagname(driver,context_title)
    title=elem2.text
    print(title)