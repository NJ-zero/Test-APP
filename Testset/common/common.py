#coding=utf-8
#author='Shichao-Dong'

# --------------
# 主要用于公共方法的编写
# --------------

from appium import webdriver
import Driver
import time
import os




def login():
    '''
    登陆返回driver
    :return:
    '''
    global driver
    driver = Driver.mydriver()
    time.sleep(2)
    a=driver.find_elements_by_class_name('android.widget.Button')
    if a:
        textfields = driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys('dongshichao')
        textfields[1].send_keys('dong')
        textfields[2].send_keys('a111111')
        driver.find_element_by_id('com.fiberhome.waiqin365.client:id/btn_login').click()
        time.sleep(4)
    else:
        time.sleep(2)
    return driver

def back():
    '''
    adb 命令
    同返回键
    :return:
    '''
    os.popen("adb shell input keyevent 4")

def get_window_size():
    '''
    获取屏幕大小
    :return: windowsize
    '''
    global windowSize
    windowSize = driver.get_window_size()
    return windowSize

def swipe_up():
    '''
    swipe up
    向上滑动
    :return:
    '''
    windowsSize = get_window_size()
    width = windowsSize.get("width")
    height = windowsSize.get("height")
    driver.swipe(width/2, height*3/4, width/2, height/4, 1000)

def screenshot(pic):
    '''
    截图
    :return:
    '''
    now=time.strftime("%y%m%d-%H-%M-%S")
    driver.get_screenshot_as_file('E:/TestAPP/Result/screenshot/'+now+pic)

def get_name(name):
    '''
    定位页面text元素
    :param name:
    :return:
    '''
    # element = driver.find_element_by_name(name)
    # return element
    findname = "//*[@text='%s']"%(name)
    print findname
    element = driver.find_element_by_xpath(findname)
    return element


def get_id(id):
    '''
    定位页面resouce-id元素
    :param id:
    :return:
    '''
    element = driver.find_element_by_id(id)
    return element

def get_ids(id):
    '''
    定位页面resouce-id元素组
    :param id:
    :return:列表
    '''
    elements = driver.find_elements_by_id(id)
    return elements









if __name__ == "__main__":
    login()