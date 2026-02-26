import json
from pages.login_page import LoginPage

def test_login(driver):

    data = json.load(open("fixtures/data.json"))

    login = LoginPage(driver)
    login.login(data["valid_user"]["username"], data["valid_user"]["password"])

    assert "inventory" in driver.current_url