from Pageobjects.loginPage import Login
from utilities import customlogger

class Test_Login_02:

    baseurl = "https:/opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "Invalid password"
    logger = customlogger.test_logDemo()

    def test_login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.loginpageobj = Login(self.driver)
        self.loginpageobj.setUserName(self.username)
        self.loginpageobj.setPassword(self.password)
        self.loginpageobj.clickLogin()
        self.confmsg = self.loginpageobj.conformationmsg()
        self.driver.close()
        if self.confmsg == "Invalid credentials":
            assert True
            self.logger.info("**********  wrong login **********")
        else:
            assert False