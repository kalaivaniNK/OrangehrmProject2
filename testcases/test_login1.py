from Pageobjects.loginPage import Login
from utilities import customlogger
from utilities.readProperties import ReadConfig

class Test_1:

    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPasswordL()

    logger = customlogger.test_logDemo()

    def test_user_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.loginPageObj = Login(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.loginPageObj.setUserName(self.username)
        self.loginPageObj.setPassword(self.password)
        self.loginPageObj.clickLogin()
        self.pimtxt = self.loginPageObj.pimpage()
        self.driver.close()
        if self.pimtxt == "PIM":
            assert True
            print("successfully login")
            self.logger.info("------- successfully login -------------")
        else:
            assert False