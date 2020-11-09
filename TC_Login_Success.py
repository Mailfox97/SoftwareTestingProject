import unittest
from selenium import webdriver


class TCLogin_Success(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\Desktop\DataScience\Soft\chromedriver.exe")

    def test_Login(self):
        driver = self.driver
        driver.get("https://online.hcmue.edu.vn/")
        driver.find_element_by_id('lbtDangnhap').click()

        driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctl00$ctl00$txtUserName').send_keys('44.01.104.201')
        driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctl00$ctl00$txtPassword').send_keys('22052000')
        driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctl00$ctl00$btLogin').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
