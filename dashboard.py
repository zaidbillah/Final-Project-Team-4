import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class TestDashboard(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_All_Hyperlink_Navbar(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") 
        driver.maximize_window()
        time.sleep(3)


        driver.find_element(By.CSS_SELECTOR,"img[alt='Itera logo']").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(1) > .nav-link").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(2) > .nav-link").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(3) > .nav-link").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(4) > .nav-link").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,".form-inline.my-2.my-lg-0 > ul > li:nth-of-type(1) > .nav-link").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,".form-inline.my-2.my-lg-0 > ul > li:nth-of-type(2) > .nav-link").click()
        

    def test_Search_Navbar(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,".form-control.mr-sm-2").send_keys("Automation") 
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,".btn.btn-secondary.my-2.my-sm-0").click()
        time.sleep(5)

    def test_TexctAreaPractice_Click(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") 
        driver.maximize_window()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(2) > .nav-link").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".body-content.container > div:nth-of-type(1)  .btn.btn-primary").click()
        time.sleep(2)
        collapse = driver.find_element(By.CSS_SELECTOR, "[class='card border-primary mb-3']:nth-child(2) pre")

        print(collapse.is_displayed())

    def test_CheckBox_RadioButton_Practice_Click(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") 
        driver.maximize_window()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(2) > .nav-link").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2)  .btn.btn-primary").click()
        time.sleep(2)
        collapse = driver.find_element(By.CSS_SELECTOR, ".collapse.show > .card.card-body")

        print(collapse.is_displayed())

    def test_Dropdown_Practice_Click(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") 
        driver.maximize_window()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(2) > .nav-link").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".body-content.container > div:nth-of-type(1)  .btn.btn-primary").click()
        time.sleep(2)
        collapse = driver.find_element(By.ID, "collapse3")

        print(collapse.is_displayed())

    def test_Practice4_Click(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") 
        driver.maximize_window()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(2) > .nav-link").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(4)  .btn.btn-primary").click()
        time.sleep(2)
        collapse = driver.find_element(By.ID, "collapse4")

        print(collapse.is_displayed())
    
    def test_input_practice(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") 
        driver.maximize_window()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(3) > .nav-link").click()
        time.sleep(3)
        driver.find_element(By.ID,"name").send_keys("Bambang")
        time.sleep(1)
        driver.find_element(By.ID,"phone").send_keys("0912388384") 
        time.sleep(1) 
        driver.find_element(By.ID,"email").send_keys("daring@mail.com") 
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("aku123") 
        time.sleep(1)
        driver.find_element(By.ID,"address").send_keys("jalan kenanga") 
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"button[name='submit']").click()
    
    def test_Dropdown_Practice(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") 
        driver.maximize_window()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(3) > .nav-link").click()
        time.sleep(3)

        x = driver.find_element(By.CSS_SELECTOR, ".custom-select")
        drop = Select(x)

        drop.select_by_value("6")
        time.sleep(4)

    def test_URadioButton_Checkbox_Practice(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/") 
        driver.maximize_window()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR,".collapse.navbar-collapse > ul > li:nth-of-type(3) > .nav-link").click()
        time.sleep(3)

        driver.find_element(By.ID, "female").click()

        driver.find_element(By.ID, "monday").click()
        driver.find_element(By.ID, "tuesday").click()
        driver.find_element(By.ID, "wednesday").click()
        driver.find_element(By.ID, "saturday").click()


        time.sleep(4)

    

    

unittest.main()