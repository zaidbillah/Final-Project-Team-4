from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net")
driver.find_element(By.CSS_SELECTOR, "a[href='/Login']").click()

# Cek apakah tombol "Forgot password" ada di halaman login
try:
    driver.find_element(By.CSS_SELECTOR, "a[href='ForgotPassword']").click()
    print("Tombol 'Forgot password' ditemukan, Anda sekarang di halaman 'Forgot password'")
except:
    print("Tidak ada tombol 'Forgot password'")