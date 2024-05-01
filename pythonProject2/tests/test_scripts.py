import time

from selenium import webdriver

from FunctionLibraries.common_methods import goto_Homepage
from config.test_setting import TestSettings
from page_objects.ab_test_link import click_AB_testing
from page_objects.add_remove_page import click_add_remove_link
from page_objects.basciauth import test_basicauth
from page_objects.broken_images import test_brokenimg_homepage
from page_objects.checkbox_homepage import test_checkbox_homepage, test_secondcheckbox
from page_objects.context_menu import test_contextmenu_homepage, test_context_title
from page_objects.digest_authentication import test_dynamicauth_homepage
from page_objects.disappearing_elements import test_disappearingelement_homepage
from page_objects.drag_drop import test_dragdrop_homepage
from page_objects.dropdown import test_dropdown_homepage, test_select_dropdownValue
from page_objects.dynamic_content import test_dynamicontents_homepage
from page_objects.dynamic_controls import test_dynamiccontrols_homepage
from page_objects.dynamic_loading import test_dynamiclanding_homepage
from page_objects.entry_ad import test_entryadd_homepage
from page_objects.exit_intent import test_exitintent_homepage


class Tests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()


    def run_tests(self):
        click_add_remove_link(self.driver)
        time.sleep(6)
        goto_Homepage(self.driver)
        click_AB_testing(self.driver)
        time.sleep(6)
        goto_Homepage(self.driver)
        time.sleep(5)
        test_basicauth(self.driver)
        time.sleep(5)
        goto_Homepage(self.driver)
        test_brokenimg_homepage(self.driver)
        time.sleep(3)
        goto_Homepage(self.driver)
        test_checkbox_homepage(self.driver)
        time.sleep(5)
        test_secondcheckbox(self.driver)
        time.sleep(6)
        goto_Homepage(self.driver)
        time.sleep(3)
        test_contextmenu_homepage(self.driver)
        time.sleep(6)
        test_context_title(self.driver)
        time.sleep(3)
        goto_Homepage(self.driver)
        time.sleep(1)
        test_dynamicauth_homepage(self.driver)
        time.sleep(3)
        goto_Homepage(self.driver)
        test_disappearingelement_homepage(self.driver)
        time.sleep(3)
        goto_Homepage(self.driver)
        test_dragdrop_homepage(self.driver)
        time.sleep(3)
        goto_Homepage(self.driver)
        test_dropdown_homepage(self.driver)
        time.sleep(6)
        test_select_dropdownValue(self.driver)
        time.sleep(6)
        goto_Homepage(self.driver)
        test_dynamicontents_homepage(self.driver)
        time.sleep(3)
        goto_Homepage(self.driver)
        test_dynamiccontrols_homepage(self.driver)
        time.sleep(3)
        goto_Homepage(self.driver)
        test_dynamiclanding_homepage(self.driver)
        time.sleep(3)
        goto_Homepage(self.driver)
        test_entryadd_homepage(self.driver)
        time.sleep(3)
        goto_Homepage(self.driver)
        test_exitintent_homepage(self.driver)
        time.sleep(3)
        goto_Homepage(self.driver)
tests = Tests()
tests.run_tests()
tests.driver.quit()