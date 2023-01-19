import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class TestLogin(unittest.TestCase): 

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_success_create_new_user_and_verify(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://itera-qa.azurewebsites.net/")
        driver.find_element(By.XPATH,"//a[text()='Login']").click()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("FajarKA") 
        time.sleep(2)
        driver.find_element(By.ID,"Password").send_keys("asd123asd") 
        time.sleep(2)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[text()='Create New']").click()
        time.sleep(2)
        driver.find_element(By.ID,"Name").send_keys("Fajar Kurniawan Alhamal") 
        time.sleep(2)
        driver.find_element(By.ID,"Company").send_keys("Fajar Jaya Makmur Sejahtera") 
        time.sleep(2)
        driver.find_element(By.ID,"Address").send_keys("Jl.Lesung VI No.44") 
        time.sleep(2)
        driver.find_element(By.ID,"City").send_keys("Depok") 
        time.sleep(2)
        driver.find_element(By.ID,"Phone").send_keys("+62123456789") 
        time.sleep(2)
        driver.find_element(By.ID,"Email").send_keys("alhamalfjr@gmail.com") 
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.NAME,"searching").send_keys("Fajar Kurniawan Alhamal")
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(5)

        verify_user_in_table = driver.find_element(By.XPATH,"//table/tbody/tr[2]/td[1]")
        print(verify_user_in_table.is_displayed())
    
    def test_edit_data_user_and_verify(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://itera-qa.azurewebsites.net/")
        driver.find_element(By.XPATH,"//a[text()='Login']").click()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("FajarKA") 
        time.sleep(2)
        driver.find_element(By.ID,"Password").send_keys("asd123asd") 
        time.sleep(2)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.NAME,"searching").send_keys("Alhamal")
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[text()='Edit']").click()
        time.sleep(2)
        driver.find_element(By.ID,"Company").send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        driver.find_element(By.ID,"Company").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.ID,"Company").send_keys("Fajar Makmur Sejahtera")
        time.sleep(2)
        driver.find_element(By.ID,"City").send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        driver.find_element(By.ID,"City").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.ID,"City").send_keys("Bogor") 
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.NAME,"searching").send_keys("Alhamal")
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(5)

        verify_Company_in_table = driver.find_element(By.XPATH,"//table/tbody/tr[2]/td[2]").is_displayed()
        verify_City_in_table = driver.find_element(By.XPATH,"//table/tbody/tr[2]/td[4]").is_displayed()
        print("Element displayed!")

    def test_verify_detail_costumers(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://itera-qa.azurewebsites.net/")
        driver.find_element(By.XPATH,"//a[text()='Login']").click()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("FajarKA") 
        time.sleep(2)
        driver.find_element(By.ID,"Password").send_keys("asd123asd") 
        time.sleep(2)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.NAME,"searching").send_keys("kurniawan")
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[text()='Details']").click()
        time.sleep(4)
    
        verify_costumer_details = driver.find_element(By.XPATH,"//h2[text()='Details']").text 
        self.assertEqual(verify_costumer_details,"Details")
        time.sleep(2)

    def test_success_delete_costumer_and_verify(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://itera-qa.azurewebsites.net/")
        driver.find_element(By.XPATH,"//a[text()='Login']").click()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("FajarKA") 
        time.sleep(2)
        driver.find_element(By.ID,"Password").send_keys("asd123asd") 
        time.sleep(2)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.NAME,"searching").send_keys("FajarKA")
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[text()='Delete']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.NAME,"searching").send_keys("FajarKA")
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(2)

        verify_deleted_user = driver.find_element(By.XPATH,"//table/tbody/tr[2]/td[1]")
        print(verify_deleted_user.is_displayed())



    def test_failed_create_new_user_with_phone_number_already_registered_and_verify(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://itera-qa.azurewebsites.net/")
        driver.find_element(By.XPATH,"//a[text()='Login']").click()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("FajarKA") 
        time.sleep(2)
        driver.find_element(By.ID,"Password").send_keys("asd123asd") 
        time.sleep(2)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[text()='Create New']").click()
        time.sleep(2)
        driver.find_element(By.ID,"Name").send_keys("Fajar Alhamal") 
        time.sleep(2)
        driver.find_element(By.ID,"Company").send_keys("Fajar Maju Sejahtera") 
        time.sleep(2)
        driver.find_element(By.ID,"Address").send_keys("Jl.Lesung VI No.44") 
        time.sleep(2)
        driver.find_element(By.ID,"City").send_keys("Depok") 
        time.sleep(2)
        driver.find_element(By.ID,"Phone").send_keys("+62789101112") 
        time.sleep(2)
        driver.find_element(By.ID,"Email").send_keys("alhamalfjr@gmail.com") 
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(2)

        verify_still_on_create_user_page = driver.find_element(By.XPATH,"//h2[text()='Create']").text
        self.assertEqual(verify_still_on_create_user_page, "Create") 
        time.sleep(2)
    
    def test_failed_create_new_user_with_email_already_registered_and_verify(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://itera-qa.azurewebsites.net/")
        driver.find_element(By.XPATH,"//a[text()='Login']").click()
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("FajarKA") 
        time.sleep(2)
        driver.find_element(By.ID,"Password").send_keys("asd123asd") 
        time.sleep(2)
        driver.find_element(By.NAME,"login").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[text()='Create New']").click()
        time.sleep(2)
        driver.find_element(By.ID,"Name").send_keys("kurniawan fajar") 
        time.sleep(2)
        driver.find_element(By.ID,"Company").send_keys("kurniawan Maju Sejahtera") 
        time.sleep(2)
        driver.find_element(By.ID,"Address").send_keys("Jl.manggis 4") 
        time.sleep(2)
        driver.find_element(By.ID,"City").send_keys("bogor") 
        time.sleep(2)
        driver.find_element(By.ID,"Phone").send_keys("+62789123") 
        time.sleep(2)
        driver.find_element(By.ID,"Email").send_keys("alhamalfjr@gmail.com") 
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(2)

        verify_still_on_create_user_page = driver.find_element(By.XPATH,"//h2[text()='Create']").text
        self.assertEqual(verify_still_on_create_user_page, "Create") 
        time.sleep(2)
    










        

    def tearDown(self): 
        self.driver.close() 
  
# execute the script 
if __name__ == "__main__": 
    unittest.main()     