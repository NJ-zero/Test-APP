#coding=utf-8
#author='Shichao-Dong'

# --------------
# 主要用于公共方法的编写
# --------------

from appium import webdriver
import Driver
import time
import os
from logs import log

log = log()

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
    try:
        element = driver.find_element_by_xpath(findname)
        driver.implicitly_wait(2)
        return element
    except:
        log.error('未定位到元素：'+'%s')%(name)

def get_id(id):
    '''
    定位页面resouce-id元素
    :param id:
    :return:
    '''
    try:
        element = driver.find_element_by_id(id)
        driver.implicitly_wait(2)
        return element
    except:
        log.error('未定位到元素：'+'%s')%(id)

def get_ids(id):
    '''
    定位页面resouce-id元素组
    :param id:
    :return:列表
    '''
    try:
        elements = driver.find_elements_by_id(id)
        driver.implicitly_wait(2)
        return elements
    except:
        log.error('未定位到元素：'+'%s')%(id)

def page(name):
    '''
    返回至指定页面
    :return:
    '''
    i=0
    while i<10:
        i=i+1
        try:
            findname = "//*[@text='%s']"%(name)
            driver.find_element_by_xpath(findname)
            driver.implicitly_wait(2)
            break
        except :
            os.popen("adb shell input keyevent 4")
            try:
                driver.find_element_by_xpath("//*[@text='工作台']")
                driver.implicitly_wait(2)
                break
            except:
                os.popen("adb shell input keyevent 4")

if __name__ == "__main__":

    login()