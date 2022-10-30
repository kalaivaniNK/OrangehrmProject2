from selenium.webdriver.common.by import By
import time

class Login:
    txtbx_email_xpath = "//input[@placeholder='Username']"
    txtbx_password_xpath = "//input[@placeholder='Password']"
    btn_login_button = "//button[normalize-space()='Login']"
# pim
    pim_add_xpath = "//button[normalize-space()='Add']"
    emp_frst_name = "//input[@placeholder='First Name']"
    emp_last_name = "//input[@placeholder='Last Name']"
    pim_save_button = "//form/div[2]//button[@type='submit']"

# personal details locators
    other_id_xpath = "//div[2]/div[1]/div[2]//div[2]/input[@class='oxd-input oxd-input--active']"
    license_no_path = "//div[2]/div[2]/div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    expiry_date = "//form/div[2]//div[2]//div/input[@placeholder='yyyy-mm-dd']"
    ssn_xpath = "//div[3]/div[1]//div[2]/input[@class='oxd-input oxd-input--active']"
    sin_xpath = "//div[3]/div[2]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    date_of_birth = "//form/div[3]/div[2]//div/input[@placeholder='yyyy-mm-dd']"
    gender_xpath = "//label[normalize-space()='Female']"
    select_nationality_xpath = "//div[@class='oxd-form-row']/div[1]/div[1]//div[@clear]"
    select_nationality_click = "//*[contains(text(),'Indian')]"
    select_married_status = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    select_married_status_click = "//*[contains(text(),'Single')]"
    military_service_xpath = "//div[4]//div[2]/input[@class='oxd-input oxd-input--active']"
    save_button_xpath = "//div[5]/button[@type='submit']"
    blood_xpath = "//form/div[1]//div[2]//div[@class='oxd-select-text oxd-select-text--active']"
    select_blood_group = "//*[contains(text(),'A+')]"
    save_button1_xpath = "//form/div[2]/button[@type='submit']"


#edit path
    click_name_path = "//div[1]/div/div[2]/div/div/input[@placeholder='Type for hints...']"
    click_emp_name = "//*[contains(text(),'kalai')]"
    search_button = "//button[@type='submit']"

    btn_edit_xpath = "//button/i[@class ='oxd-icon bi-pencil-fill']"

    edit_married_xpath = "//*[contains(text(),'Married')]"
#delete
    delete_user = "//i[@class='oxd-icon bi-trash']"
    confirm_delete = "//div[3]/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def setLogin(self, username,password):
        self.driver.find_element(By.XPATH, self.txtbx_email_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.txtbx_password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.btn_login_button).click()

    def pim(self, firstName, lastName):
        self.driver.find_element(By.XPATH, self.pim_add_xpath).click()
        self.driver.find_element(By.XPATH, self.emp_frst_name).send_keys(firstName)
        self.driver.find_element(By.XPATH, self.emp_last_name).send_keys(lastName)
        self.driver.find_element(By.XPATH, self.pim_save_button).click()

    def peronal_details(self, otherid, licenseno, expirydate, ssn, sin, dob, militaryservice):
        self.driver.find_element(By.XPATH, self.other_id_xpath).send_keys(otherid)
        self.driver.find_element(By.XPATH, self.license_no_path).send_keys(licenseno)
        self.driver.find_element(By.XPATH, self.expiry_date).send_keys(expirydate)
        self.driver.find_element(By.XPATH, self.ssn_xpath).send_keys(ssn)
        self.driver.find_element(By.XPATH, self.sin_xpath).send_keys(sin)
        self.driver.find_element(By.XPATH, self.date_of_birth).send_keys(dob)
        self.driver.find_element(By.XPATH, self.gender_xpath).click()
        self.driver.find_element(By.XPATH, self.select_nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.select_nationality_click).click()
        self.driver.find_element(By.XPATH, self.select_married_status).click()
        self.driver.find_element(By.XPATH, self.select_married_status_click).click()
        self.driver.find_element(By.XPATH, self.military_service_xpath).send_keys(militaryservice)
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
        self.driver.find_element(By.XPATH, self.blood_xpath).click()
        self.driver.find_element(By.XPATH, self.select_blood_group).click()
        self.driver.find_element(By.XPATH, self.save_button1_xpath).click()

    def pim_edit(self,name):
        self.driver.find_element(By.XPATH,self.click_name_path).send_keys(name)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.click_emp_name).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.search_button).click()

    def edit(self):
        self.driver.find_element(By.XPATH, self.btn_edit_xpath).click()


    def editMaritalStatus(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.select_married_status).click()
        self.driver.find_element(By.XPATH, self.edit_married_xpath).click()
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def deleteuser(self):
        self.driver.find_element(By.XPATH,self.delete_user).click()
        self.driver.find_element(By.XPATH,self.confirm_delete).click()