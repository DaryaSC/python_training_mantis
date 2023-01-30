from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)

    def open_home_page(self):
        self.driver.get(self.base_url)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False


    def destroy(self):
        self.driver.quit()
