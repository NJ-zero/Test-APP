#coding=utf-8
#author='Shichao-Dong'


import os
import readConfig

conf = readConfig.Readconfig()

class readCmd:
    def __init__(self):
        self.get_device = conf.getcmdValue('viewPhone')
        self.get_Version = conf.getcmdValue('viewAndroid')
        self.startServer = conf.getcmdValue('startServer')

    def get_deviceName(self):
        values = os.popen(self.get_device).readlines()
        dev = values[1].split()[0]
        if len(values)-2 == 1:
            print dev
            return dev
        else:
            print 'No device found'

    def get_platformVersion(self):
        values = os.popen(self.get_Version).readlines()

        if values != '':
            Version=values[0].split('=')[1]
            print Version
            return Version.strip()
        else:
            print 'No device found'



if __name__ == '__main__':
    cmd = readCmd()
    cmd.get_deviceName()
    cmd.get_platformVersion()