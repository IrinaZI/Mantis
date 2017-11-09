import pytest
import json
import os.path
import ftputil
from fixture.application import Application


fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),file )
        with open(config_file) as conf:
            target = json.load(conf)
    return target

@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture(scope="session", autouse=True)
def configure_server(request, config):
    install_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    def fin():
        restore_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    request.addfinalizer(fin)

def install_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remoute:
        if remoute.path.isfile("config_inc.php.bak"):
            remoute.remove("config_inc.php.bak")
        if remoute.path.isfile("config_inc.php"):
            remoute.rename("config_inc.php", "config_inc.php.bak")
        remoute.upload(os.path.join(os.path.dirname(__file__), "resourse/config_inc.php"), "config_inc.php")

def restore_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remoute:
        if remoute.path.isfile("config_inc.php.bak"):
            if remoute.path.isfile("config_inc.php"):
                remoute.remove("config_inc.php")
            remoute.rename("config_inc.php.bak", "config_inc.php")


@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=config['web']["baseUrl"])
    fixture.session.ensure_Login(username=config['web']["username"], password=config['web']["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_Logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")



