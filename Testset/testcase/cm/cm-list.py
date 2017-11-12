#coding=utf-8
#author='Shichao-Dong'

import sys,os
reload(sys)
sys.path.append('E:\TestAPP\Testset')
from common.logs import log
from appium import webdriver
import unittest
import time
from common import common

class visit_temp(unittest.TestCase):
    log = log()

    log.info(u'开始客户管理列表部分的测试')
    @classmethod
    def setUpClass(cls):
        cls.driver=common.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_1launchstore(self):

        # a = "//*[@text='%s']"%('终端门店')
        # self.driver.find_element_by_xpath(a).click()
        common.screenshot(u'工作台.png')
        common.get_name('终端门店').click()

        time.sleep(2)

if __name__=="__main__":
    unittest.main()
