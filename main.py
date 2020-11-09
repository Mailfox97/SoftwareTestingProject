from selenium import webdriver

driver = webdriver.Chrome("G:\chromedriver\chromedriver.exe")

driver.get("https://online.hcmue.edu.vn/")

driver.find_element_by_id('lbtDangnhap').click()

driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctl00$ctl00$txtUserName').send_keys('44.01.104.201')
driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctl00$ctl00$txtPassword').send_keys('22052000')
driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctl00$ctl00$btLogin').click()


