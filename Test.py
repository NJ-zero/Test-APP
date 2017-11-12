#coding=utf-8
#author='Shichao-Dong'

import time
import sys,os
reload(sys)
sys.path.append('E:\TestAPP\Testset')
from common.logs import log
from appium import webdriver

# log = log()
# log.info('hshahah')
# log.debug('debug')

now=time.strftime("%Y%m%d-%H%M%S")
print now