import unittest
import TC_Login_Fail
import TC_Login_Success
import os
import HTMLTestRunner.HTMLTestRunner

direct = os.getcwd()

class TS_Login(unittest.TestCase):
    def test_Login(self):

        TS_test = unittest.TestSuite()
        TS_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TC_Login_Success.TCLogin_Success),
            unittest.defaultTestLoader.loadTestsFromTestCase(TC_Login_Fail.TCLogin_Fail),
        ])
        outfile = open(direct + "\TS_test.html", "w")
        runner1 = HTMLTestRunner.HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Login Test'
        )

        runner1.run(TS_test)


if __name__ == '__main__':
    unittest.main()
