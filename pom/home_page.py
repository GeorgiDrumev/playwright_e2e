from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://playwright.dev/"
        self.get_started_link = self.page.get_by_role("link", name="Get started")
        self.installation_heading = self.page.get_by_role("heading", name="Installation")

    def navigate(self):
        self.page.goto(self.url)

    def verify_title(self):
        expect(self.page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    def click_get_started(self):
        self.get_started_link.click()

    def verify_installation_page(self):
        expect(self.installation_heading).to_be_visible()