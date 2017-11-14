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

    log.info(u'开始高级拜访的测试')
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

    def test_1launchvisit(self):
        common.get_name('高级拜访').click()
        try:
            self.assertTrue(common.find_name(u'临时拜访'))
        except Exception,e:
            print e
            log.error('进入高级拜访模块失败')
            common.screenshot("launchvisit.png")

    def test_2temp(self):
        common.get_name('临时拜访').click()
        if common.find_name('显示全部客户'):
            common.get_name('显示全部客户').click()

        common.page('高级拜访')



if __name__=="__main__":
    unittest.main()