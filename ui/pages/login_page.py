class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "input[value='Log In']"

    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def logout(self):
        self.page.click("text=Log Out")