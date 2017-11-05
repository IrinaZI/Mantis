from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_to_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='/mantisbt - 1.2.19/manage_overview_page.php']").click()
        wd.find_element_by_css_selector("a[href='/mantisbt-1.2.19/manage_proj_page.php']").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_to_project_page()
        wd.find_element_by_value("Create New Project").click()
        self.fill_project_form(contact)
        wd.find_element_by_value("Add Project").click()
        self.open_to_project_page()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.Name)
        self.change_field_value("status", project.Status)
        self.change_field_value("inherit_global", project.Inherit_global)
        self.change_field_value("view_state", project.View_status)
        self.change_field_value("description", project.Description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
