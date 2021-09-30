# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddRole(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)

    def test_add_role(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1280,609 | ]]
        driver.get("http://10.70.36.234/#/login")
        driver.find_element_by_id("auth-login-field-username").click()
        driver.find_element_by_id("auth-login-field-username").clear()
        driver.find_element_by_id("auth-login-field-username").send_keys("test")
        driver.find_element_by_css_selector("div.v-card__title.card__title.mb-2").click()
        driver.find_element_by_id("auth-login-field-password").click()
        driver.find_element_by_id("auth-login-field-password").clear()
        driver.find_element_by_id("auth-login-field-password").send_keys("123")
        driver.find_element_by_css_selector("span.v-btn__content").click()
        driver.find_element_by_css_selector("#main-layout-navigation-user_roles > div.v-list-item__content > div.v-list-item__title").click()
        driver.find_element_by_css_selector("button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default > span.v-btn__content").click()
        driver.find_element_by_id("input-469").click()
        driver.find_element_by_css_selector("div.col.col-12 > div.row").click()
        driver.find_element_by_id("input-469").clear()
        driver.find_element_by_id("input-469").send_keys("test")
        driver.find_element_by_css_selector("button.primary.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default > span.v-btn__content").click()
        driver.find_element_by_id("main-layout-navigation-btn-logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.driver.quit()


