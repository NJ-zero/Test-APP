#coding=utf-8
#author='Shichao-Dong'

import sys,os
reload(sys)
sys.path.append(r'E:\TestAPP\Testset\testcase')
import unittest
import HTMLTestRunner
import time
from cm.test_cm_list import store_list
from visit.test_visit_temp import visit_temp


def testsuit():
    suite = unittest.TestSuite()
    suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(store_list),
                   unittest.defaultTestLoader.loadTestsFromTestCase(visit_temp)



                   ])


    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    now=time.strftime("%y-%m-%d-%H-%M-%S")
    dir = r'E:\\TestAPP\\Result\\report\\'
    filename=dir + now +'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test result',description=u'result:')

    runner.run(suite)
    fp.close()

if __name__ =="__main__":
    testsuit()