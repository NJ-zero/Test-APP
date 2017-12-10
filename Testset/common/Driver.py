#coding=utf-8
#author='Shichao-Dong'

# ------------
# 获取driver并返回
# ------------


from appium import webdriver
from selenium.common.exceptions import WebDriverException
import readConfig
import readCmd

conf = readConfig.Readconfig()
cmd = readCmd.readCmd()


deviceName = cmd.get_deviceName()
platformVersion = cmd.get_platformVersion().encode('ascii')
platformName = conf.getConfigValue('platformName')
appPackage = conf.getConfigValue('appPackage').encode('ascii')
appActivity = conf.getConfigValue('appActivity').encode('ascii')
print appPackage

def mydriver():
    desired_caps = {
                'platformName':platformName,'deviceName':deviceName, 'platformVersion':platformVersion,
                'appPackage':appPackage,'appActivity':appActivity,
                'unicodeKeyboard':True,'resetKeyboard':True,'noReset':True
                }
    try:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        return driver
    except WebDriverException:
        print 'No driver'


if __name__ == "__main__":

    mydriver()
