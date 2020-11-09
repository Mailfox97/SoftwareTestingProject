import XLUtils
from selenium import webdriver
import os

driver = webdriver.Chrome("D:\Desktop\DataScience\Soft\chromedriver.exe")
driver.get("https://online.hcmue.edu.vn")
direct = os.getcwd()
path = direct + "\logintest.xlsx"
#print(path)
rows=XLUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    driver.find_element_by_id('lbtDangnhap').click()
    #driver.find_element_by_id('lbtDangnhap').click()
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)


    driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctl00$ctl00$txtUserName').send_keys(username)
    driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctl00$ctl00$txtPassword').send_keys(password)
    driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctl00$ctl00$btLogin').click()

    if r == 2:
        driver.implicitly_wait(10)
        if driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_ctl00_lblThongbao').is_displayed():
            print("Passed")
            XLUtils.writeData(path, 'Sheet1', r, 3, "passed")
        else:
            print("Failed")
            XLUtils.writeData(path, 'Sheet1', r, 3, "failed")
    else:
        driver.implicitly_wait(10)
        if driver.find_element_by_id("ContentPlaceHolder1_ctl00_ctl00_tdError").is_displayed():
            print("Passed")
            XLUtils.writeData(path, 'Sheet1', r, 3, "passed")
        else:
            print("Failed")
            XLUtils.writeData(path, 'Sheet1', r, 3, "failed")
    driver.find_element_by_id('lbtDangnhap').click()

