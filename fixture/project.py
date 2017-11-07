from model.project import Project
import time

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='/mantisbt-1.2.19/manage_overview_page.php']").click()
        wd.find_element_by_css_selector("a[href='/mantisbt-1.2.19/manage_proj_page.php']").click()

    def create(self, project):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='/mantisbt-1.2.19/manage_overview_page.php']").click()
        wd.find_element_by_css_selector("a[href='/mantisbt-1.2.19/manage_proj_page.php']").click()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.open_project_page()
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

    project_cache = None

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        if self.project_cache is None:
             if len(wd.find_elements_by_css_selector("a[href^='manage_proj_edit_page.php?project_i']")) > 0:
                self.project_cache = []
                for element in wd.find_elements_by_css_selector("a[href^='manage_proj_edit_page.php?project_i']"):
                    name = element.text
                    id = element.get_attribute("href")[70:]
                    self.project_cache.append(Project(id = id, name=name, inherit_global=None,
                                                     view_status=None, description=None))
             else:
                 self.project_cache = []
             return list(self.project_cache)


    def del_project(self, index):
        wd = self.app.wd
        self.open_project_page()
        del_proj=wd.find_elements_by_css_selector("a[href^='manage_proj_edit_page.php?project_i']")[index]
        deluid = del_proj.get_attribute("href")[33:]
        print(deluid)
        wd.find_element_by_css_selector("a[href='%s']" % deluid).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        time.sleep(1)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.open_project_page()