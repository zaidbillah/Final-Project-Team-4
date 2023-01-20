import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from data import datanya


class TestLoginRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_TCN8(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            datanya.nama)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            datanya.password)  # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.btn:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # button create, isi data di skip karena input blank data
        time.sleep(1)
        driver.find_element(By.ID, "Name").send_keys("1122334455")
        time.sleep(1)
        driver.find_element(By.ID, "Company").send_keys("1234567890")
        time.sleep(1)
        driver.find_element(By.ID, "Address").send_keys("1234567890")
        time.sleep(1)
        driver.find_element(By.ID, "City").send_keys("1234567890")
        time.sleep(1)
        driver.find_element(By.ID, "Phone").send_keys("082124578458")
        time.sleep(1)
        driver.find_element(By.ID, "Email").send_keys("1234567890")
        time.sleep(1)
        # only input Email on create new customer
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)
        driver.find_element(By.ID, "searching").send_keys("1122334455")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)


unittest.main()
