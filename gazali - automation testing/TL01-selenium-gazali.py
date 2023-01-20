from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net")
driver.find_element(By.CSS_SELECTOR, "a[href='/Login']").click()

driver.find_element(By.ID,"Username").send_keys("admin")
driver.find_element(By.ID, "Password").send_keys("admin")

#driver.find_element_by_class_name("btn btn-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# Cek kondisi login
if "https://itera-qa.azurewebsites.net/Dashboard" in driver.current_url:
    print("Login berhasil, Anda sekarang berada di halaman dashboard")
else:
    print("Login gagal, pastikan username dan password yang Anda masukkan benar")
