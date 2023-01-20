from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net")
driver.find_element(By.CSS_SELECTOR, "a[href='/Login']").click()

driver.find_element(By.ID,"Username").send_keys("masukaja")
driver.find_element(By.ID, "Password").send_keys("M45uk4j4")
password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password_field.send_keys("password")
password_field.send_keys(Keys.RETURN)

#driver.find_element_by_class_name("btn btn-primary").click()
#driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# Cek kondisi login
if "https://itera-qa.azurewebsites.net/Dashboard" in driver.current_url:
    print("passed")
else:
    print("failed")
