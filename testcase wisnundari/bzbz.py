
    def test_TCN1(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            "windadyahayu")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            "1234")  # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.btn:nth-child(1)").click()
        time.sleep(1)
        # button createnew pada dashboard
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(1)
        # button create, isi data di skip karena input blank data
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)

    def test_TCN2(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            "windadyahayu")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            "1234")  # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.btn:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # button create, isi data di skip karena input blank data
        time.sleep(1)
        driver.find_element(By.ID, "Name").send_keys("riskanti")
        time.sleep(1)
        # only input name on create new customer
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)
        driver.find_element(By.ID, "searching").send_keys("riskanti")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)

    def test_TCN3(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            "windadyahayu")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            "1234")  # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.btn:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # button create, isi data di skip karena input blank data
        time.sleep(1)
        driver.find_element(By.ID, "Company").send_keys("riskacom")
        time.sleep(1)
        # only input Company on create new customer
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)

    def test_TCN4(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            "windadyahayu")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            "1234")  # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.btn:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # button create, isi data di skip karena input blank data
        time.sleep(1)
        driver.find_element(By.ID, "Address").send_keys("Jalan Raya Bomang")
        time.sleep(1)
        # only input Address on create new customer
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)

    def test_TCN5(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            "windadyahayu")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            "1234")  # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.btn:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # button create, isi data di skip karena input blank data
        time.sleep(1)
        driver.find_element(By.ID, "City").send_keys("Citayam City")
        time.sleep(1)
        # only input City on create new customer
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)

    def test_TCN6(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            "windadyahayu")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            "1234")  # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.btn:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # button create, isi data di skip karena input blank data
        time.sleep(1)
        driver.find_element(By.ID, "Phone").send_keys("082124578458")
        time.sleep(1)
        # only input Phone on create new customer
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)

    def test_TCN7(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            "windadyahayu")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            "1234")  # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.btn:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # button create, isi data di skip karena input blank data
        time.sleep(1)
        driver.find_element(By.ID, "Email").send_keys("riskanti@gmail.com")
        time.sleep(1)
        # only input Email on create new customer
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)

    def test_TCN8(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            "windadyahayu")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            "1234")  # isi password
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

    def test_TCN9(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            "windadyahayu")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            "1234")  # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.btn:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # button create, isi data di skip karena input blank data
        time.sleep(1)
        driver.find_element(By.ID, "Name").send_keys("bagus")
        time.sleep(1)
        driver.find_element(By.ID, "Company").send_keys("bagustech")
        time.sleep(1)
        driver.find_element(By.ID, "Address").send_keys("Jalan Raya Citayam")
        time.sleep(1)
        driver.find_element(By.ID, "City").send_keys("Citayam")
        time.sleep(1)
        driver.find_element(By.ID, "Phone").send_keys("082124578458")
        time.sleep(1)
        driver.find_element(By.ID, "Email").send_keys("baguscitayam")
        time.sleep(1)
        # only input Email on create new customer
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)
        driver.find_element(By.ID, "searching").send_keys("bagus")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)

    def test_TCN10(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, ".form-inline > ul:nth-child(1) > li:nth-child(2)").click()
        driver.find_element(By.ID, "Username").send_keys(
            "windadyahayu")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "Password").send_keys(
            "1234")  # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input.btn:nth-child(1)").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # button create, isi data di skip karena input blank data
        time.sleep(1)
        driver.find_element(By.ID, "Name").send_keys(
            "sultan agung raden adiguna bagus wihandono dirgantara putra andhika aulia agung raja mulia wijayakusuma nusantara Indonesia ke XII")
        time.sleep(1)
        driver.find_element(By.ID, "Company").send_keys(
            "bagustech raden adiguna bagus wihandono dirgantara putra andhika aulia agung raja mulia")
        time.sleep(1)
        driver.find_element(By.ID, "Address").send_keys(
            "Jalan Raya Citayam raden adiguna bagus wihandono dirgantara putra andhika aulia agung raja mulia")
        time.sleep(1)
        driver.find_element(By.ID, "City").send_keys("Citayam")
        time.sleep(1)
        driver.find_element(By.ID, "Phone").send_keys("082124578458")
        time.sleep(1)
        driver.find_element(By.ID, "Email").send_keys("baguscitayam")
        time.sleep(1)
        # only input Email on create new customer
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)
        driver.find_element(By.ID, "searching").send_keys("bagus")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input.btn").click()
        time.sleep(2)
