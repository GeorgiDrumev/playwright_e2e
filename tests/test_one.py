from playwright.sync_api import Page
from pom.home_page import HomePage

def test_has_title(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.verify_title()

def test_get_started_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_get_started()
    home_page.verify_installation_page()