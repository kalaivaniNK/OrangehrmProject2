from Pageobjects.PIMpage import Login
from utilities import customlogger

class Test_1:

    baseurl = "https:/opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

# pim
    firstname = "kalai"
    lastName = "vani"

# personal details
    otherid = "123"
    licenseno = "456"
    expirydate = "2025-05-10"
    ssn = "867"
    sin = "909"
    dob = "1998-08-17"
    militaryservice = "no"

    logger = customlogger.test_logDemo()



    def test_add_employee(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.loginPageObj = Login(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.loginPageObj.setLogin(self.username,self.password)
        self.loginPageObj.pim(self.firstname,self.lastName)
        self.logger.info("***********  the new employee is added  **********")
        self.loginPageObj.peronal_details(self.otherid, self.licenseno, self.expirydate, self.ssn, self.sin, self.dob,self.militaryservice)
        self.logger.info("**********  personal details are added  **********")