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

class store_list(unittest.TestCase):
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
        common.screenshot(u'工作台.png')
        common.get_name('终端门店').click()

    def test_2addstore(self):
        log.info('开始新增终端门店')

        common.get_id('com.fiberhome.waiqin365.client:id/cm_topbar_tv_right').click()
        common.get_name('点击输入').send_keys('test-APP')
        common.get_name('提交').click()
        common.page('工作台')

if __name__=="__main__":
    unittest.main()
