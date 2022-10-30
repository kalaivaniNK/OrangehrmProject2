from Pageobjects.PIMpage import Login
from utilities import customlogger

class Test_1:

    baseurl = "https:/opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    name= "kalai"

    logger = customlogger.test_logDemo()
    def test_edit_employee(self ,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.loginPageObj = Login(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.loginPageObj.setLogin(self.username ,self.password)
        self.loginPageObj.pim_edit(self.name)
        self.loginPageObj.edit()
        self.loginPageObj.editMaritalStatus()
        self.logger.info("***********  successfully edit the marital status **********")