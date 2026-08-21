class RegisterPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/register.htm")

    def register_new_user(self, username, password):
        self.page.fill("#customer\\.firstName", "Jora")
        self.page.fill("#customer\\.lastName", "Test")
        self.page.fill("#customer\\.address\\.street", "123 Test St")
        self.page.fill("#customer\\.address\\.city", "Ottawa")
        self.page.fill("#customer\\.address\\.state", "ON")
        self.page.fill("#customer\\.address\\.zipCode", "K1A0A1")
        self.page.fill("#customer\\.phoneNumber", "6135551234")
        self.page.fill("#customer\\.ssn", "123456789")
        self.page.fill("#customer\\.username", username)
        self.page.fill("#customer\\.password", password)
        self.page.fill("#repeatedPassword", password)
        self.page.click("input[value='Register']")