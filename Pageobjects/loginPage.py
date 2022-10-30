from selenium.webdriver.common.by import By


class Login:
    txtbx_email_xpath = "//input[@placeholder='Username']"
    txtbx_password_xpath = "//input[@placeholder='Password']"
    btn_login_button = "//button[normalize-space()='Login']"

    pim_path = "//h6"

    confirmation_xpath = "//p[text()='Invalid credentials']"




    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.txtbx_email_xpath).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtbx_password_xpath).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_button).click()

    def pimpage(self):
        return self.driver.find_element(By.XPATH,self.pim_path).text

    def conformationmsg(self):
        return self.driver.find_element(By.XPATH,self.confirmation_xpath).text

