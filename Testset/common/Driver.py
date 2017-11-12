#coding=utf-8
#author='Shichao-Dong'

# ------------
# 获取driver并返回
# ------------


from appium import webdriver
from selenium.common.exceptions import WebDriverException

def mydriver():
    desired_caps = {
                'platformName':'Android',
                'deviceName':'G40GLD4572500169',
                'platformVersion':'6.0',
                'appPackage':'com.fiberhome.waiqin365.client',
                'appActivity':'com.waiqin365.base.login.LoginSplashActivity',
                'unicodeKeyboard':True,
                'resetKeyboard':True,
                'noReset':True
                }
    try:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        return driver
    except WebDriverException:
        print 'No driver'



