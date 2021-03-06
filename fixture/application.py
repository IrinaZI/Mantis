
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.mail import MailHelper
from fixture.signup import SignupHelper
from fixture.soap import SoapHelper






class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.config = config
        self.soap = SoapHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.base_url=config['web']['baseUrl']


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_login_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("http://localhost/mantisbt-1.2.19/login_page.php") and wd.find_element_by_id("LoginForm")):
            wd.get(self.base_url)


    def destroy (self):
        self.wd.quit()