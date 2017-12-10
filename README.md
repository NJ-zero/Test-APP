# Test-APP
python+appium的安卓UI自动化测试框架

## 环境说明

windows + python2.7 + appium 1.6+

## 整体框架说明
![image](https://github.com/NJ-zero/Test-APP/raw/master/app.png)

#### Result主要存放测试结果相关文件

- logs----------存放运行日志（来源于logging模块）
- report--------存放html报告
- screenshot----存放失败截图
#### Testset主要存放用例相关文件
- common--------存放公共文件
    - common.py公共方法，定位元素，截图，返回指定页面等
    - config.ini 配置文件
    - Driver.py 根据配置文件获取driver
    - logs.py 日志模块，定义日志level及显示的格式
    - readxxx.py 用来读取配置文件
- testcase------存放测试用例
    - cm即客户模块，visit即拜访模块，一个模块一个文件夹
- HTMLTestRunner.py用来生成测试报告
- runtest.py 用来批量执行用例