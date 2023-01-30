from selenium.webdriver.common.by import By
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def create(self, project):
        self.open_manage_project_page()
        self.app.driver.find_element(By.CSS_SELECTOR, "input[value='Create New Project']").click()
        self.fill_group_form(project)
        self.app.driver.find_element(By.CSS_SELECTOR, "input[value='Add Project']").click()
        self.open_manage_project_page()
        self.project_cache = None

    def fill_group_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).clear()
            self.app.driver.find_element(By.NAME, field_name).send_keys(text)

    def open_manage_project_page(self):
        if not (self.app.driver.current_url.endswith("/manage_proj_page.php")):
            self.app.driver.find_element(By.LINK_TEXT, "Manage").click()
            self.app.driver.find_element(By.LINK_TEXT, "Manage Projects").click()

    def get_project_list(self):
        if self.project_cache is None:
            self.open_manage_project_page()
            self.project_cache = []
            for element in self.app.driver.find_elements\
                        (By.XPATH, "//table[@class='width100']/tbody/tr[@class='row-1' or @class='row-2']"):
                name = element.find_element(By.XPATH, "td[1]").text
                description = element.find_element(By.XPATH, "td[5]").text
                link = element.find_element(By.XPATH, "td[1]/a").get_attribute("href")
                id = link.split("id=")[1]
                self.project_cache.append(Project(name=name, id=id, description=description))
        return list(self.project_cache)

    def delete_project_by_name(self, name):
        self.open_manage_project_page()
        self.app.driver.find_element(By.LINK_TEXT, name).click()
        self.app.driver.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        self.app.driver.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        self.project_cache = None

    def count(self):
        self.open_manage_project_page()
        return len(self.app.driver.find_elements
                   (By.XPATH, "//table[@class='width100']/tbody/tr[@class='row-1' or @class='row-2']"))
