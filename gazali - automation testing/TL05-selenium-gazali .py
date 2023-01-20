from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net")
driver.find_element(By.CSS_SELECTOR, "a[href='/Login']").click()

driver.find_element(By.ID,"Username").send_keys("salah")
driver.find_element(By.ID, "Password").send_keys("passnyasalah")

#driver.find_element_by_class_name("btn btn-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# Cek kondisi login
if "alert-danger" in driver.page_source:
    print("passed")
else:
    print("failed")