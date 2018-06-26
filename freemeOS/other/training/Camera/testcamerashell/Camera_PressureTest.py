#!/usr/bin/python
# -*- coding: UTF-8 -*-
#! python2.7
#
import os
from uiautomator import Device
import time
import sys
from os import popen
# if not os.path.exists('e:/%s'%deva):
# 	os.mkdir(r'e:/%s/'%deva)
# if not os.path.exists('e:/%s/screenshot'%deva):
# 	os.mkdir(r'e:/%s/screenshot'%deva)

class Camera_pressureTest:
    def __init__(self):
        self.Id = self.getDeviceId()
        self.temp = []

    def getDeviceId(self):
        devices_get=popen('adb devices').read()
        devices_get=devices_get.split('\n')
        if(len(devices_get)==3):
            print('No device!')
        elif(len(devices_get)==4):
            print('just one device!')
            device_id=devices_get[1].split('\t')[0]
            return device_id
        else:
            temp = []
            devices_num = len(devices_get) - 3
            print('There are '+str(devices_num)+' devices, which one is target device?')
            for i in range(devices_num):
                device_id = devices_get[i+1].split('\t')[0]
                temp.append(device_id)
                print(device_id)
                print temp
                device_id = raw_input('input devices_id:')
                return device_id
            if device_id not in temp:
                raise Exception("devices_id not exists,exit")
            # return device_id

        # deva = devices_id
        # if not os.path.exists('e:/%s'%deva):
        # 	os.mkdir(r'e:/%s/'%deva)
        # if not os.path.exists('e:/%s/screenshot'%deva):
        # 	os.mkdir(r'e:/%s/screenshot'%deva)
        # if not os.path.exists('e:/%s/error'%deva):
        # 	os.mkdir(r'e:/%s/error'%deva)

    def getDeava(self):
        deva = self.Id
        print("deva = ",deva)
        if not os.path.exists('%s'%deva):
            os.mkdir('%s/'%deva)
            if not os.path.exists('%s/screenshot'%deva):
                os.mkdir(r'%s/screenshot'%deva)
                if not os.path.exists('%s/error'%deva):
                    os.mkdir(r'%s/error'%deva)
                    # 后摄相机退出进入
                    def EnterExit(self):
                        dev = Device(self.Id)
                        try:
                            for temp6 in range(1000):
                                print('%sEnterExit' %(temp6+1))
                                dev(text='相机').click()
                                time.sleep(2)
                                dev.screenshot(r'%s/screenshot/%sEnterExit.png' %(self.Id,(temp6+1)))
                                time.sleep(1)
                                os.system('adb shell input keyevent BACK')
                                os.system('adb shell input keyevent BACK')
                                os.system('adb shell input keyevent HOME')
                                time.sleep(1)
                        except Exception , e:
                            print('error',e)
                            dev.screenshot(r'%s/error/errorEnterExit.png' %(self.Id))
                            os.system('adb shell input keyevent BACK')
                            os.system('adb shell input keyevent BACK')
                            os.system('adb shell input keyevent HOME')
                            # 前摄相机退出进入
                            def qianEnterExit(self):
                                dev = Device(self.Id)
                                try:
                                    for temp6 in range(1000):
                                        print('%sqianEnterExit' %(temp6+1))
                                        dev(text='相机').click()
                                        time.sleep(2)
                                        dev(resourceId='com.freeme.camera:id/camera_toggle_button').click()
                                        time.sleep(2)
                                        dev.screenshot(r'%s/screenshot/%sqianEnterExit.png' %(self.Id,(temp6+1)))
                                        time.sleep(1)
                                        os.system('adb shell input keyevent BACK')
                                        os.system('adb shell input keyevent BACK')
                                        os.system('adb shell input keyevent HOME')
                                        time.sleep(1)
                                except Exception , e:
                                    print('error',e)
                                    dev.screenshot(r'%s/error/errorqianEnterExit.png' %(self.Id))
                                    os.system('adb shell input keyevent BACK')
                                    os.system('adb shell input keyevent BACK')
                                    os.system('adb shell input keyevent HOME')
                                    # 前后摄切换
                                    def FrontRear(self):
                                        dev = Device(self.Id)
                                        try:
                                            dev(text='相机').click()
                                            time.sleep(2)
                                            for temp6 in range(1000):
                                                print('%sFrontRear' %(temp6+1))
                                                dev(resourceId="com.freeme.camera:id/camera_toggle_button").click()
                                                time.sleep(2)
                                                dev(resourceId="com.freeme.camera:id/camera_toggle_button").click()
                                                time.sleep(2)
                                                dev.screenshot(r'%s/screenshot/%sFrontRear.png' %(self.Id,(temp6+1)))
                                                time.sleep(1.5)
                                        except Exception , e:
                                            print('error',e)
                                            dev.screenshot(r'%s/error/errorFrontRear.png' %(self.Id))
                                            os.system('adb shell input keyevent BACK')
                                            os.system('adb shell input keyevent BACK')
                                            os.system('adb shell input keyevent HOME')

# 后摄连续拍照
def TakePhoto(self):
    dev = Device(self.Id)
    try:
        dev(text='相机').click()
        time.sleep(2)
        for temp4 in range(1000):
            print('%sTakePhoto' %(temp4+1))
            dev(resourceId='com.freeme.camera:id/shutter_button').click()
            time.sleep(1)
            dev.screenshot(r'%s/screenshot/%sTakePhoto.png' %(self.Id,(temp4+1)))
            time.sleep(1)
    except Exception , e:
        print('error',e)
        dev.screenshot(r'%s/error/errorTakePhoto.png' %(self.Id))
        dev.press.BACK()
        os.system('adb shell input keyevent BACK')
        os.system('adb shell input keyevent BACK')
        os.system('adb shell input keyevent HOME')
        # 前摄连续拍照
        def proactive(self):
            dev = Device(self.Id)
            try:
                dev(text='相机').click()
                time.sleep(2)
                dev(resourceId='com.freeme.camera:id/camera_toggle_button').click()
                time.sleep(2)
                for temp6 in range(1000):
                    print('%sproactive' %(temp6+1))
                    dev(resourceId='com.freeme.camera:id/shutter_button').click()
                    time.sleep(1.5)
                    dev.screenshot(r'%s/screenshot/%sproactive.png' %(self.Id,(temp6+1)))
                    time.sleep(1)
            except Exception , e:
                print('error',e)
                dev.screenshot(r'%s/error/errorproactive.png')
                os.system('adb shell input keyevent BACK')
                os.system('adb shell input keyevent BACK')
                os.system('adb shell input keyevent HOME')
                #虚化拍照切换
                def xuhuaqiehuanpaizhao(self):
                    dev = Device(self.Id)
                    try:
                        dev(text='相机').click()
                        time.sleep(2)
                        for temp6 in range(1000):
                            print('%sxuhuaqiehuanpaizhao' %(temp6+1))
                            dev(resourceId='com.freeme.camera:id/freeme_bv_button').click()
                            time.sleep(1.5)
                            dev(resourceId='com.freeme.camera:id/freeme_bv_button').click()
                            time.sleep(1.5)
                            dev.screenshot(r'%s/screenshot/%sxuhuaqiehuanpaizhao.png' %(self.Id,(temp6+1)))
                            time.sleep(1)
                    except Exception , e:
                        print('error',e)
                        dev.screenshot(r'%s/error/errorxuhuaqiehuanpaizhao.png')
                        dev.press.BACK()
                        os.system('adb shell input keyevent BACK')
                        os.system('adb shell input keyevent BACK')
                        os.system('adb shell input keyevent HOME')
                        #虚化拍照
                        def xuhuapaizhao(self):
                            dev = Device(self.Id)
                            try:
                                dev(text='相机').click()
                                time.sleep(2)
                                dev(resourceId='com.freeme.camera:id/freeme_bv_button').click()
                                time.sleep(2)
                                for temp6 in range(1000):
                                    print('%sxuhuapaizhao' %(temp6+1))
                                    dev(resourceId='com.freeme.camera:id/shutter_button').click()
                                    time.sleep(1.5)
                                    dev.screenshot(r'%s/screenshot/%sxuhuapaizhao.png' %(self.Id,(temp6+1)))
                                    time.sleep(1)
                            except Exception , e:
                                print('error',e)
                                dev.screenshot(r'%s/error/errorxuhuapaizhao.png')
                                dev.press.BACK()
                                os.system('adb shell input keyevent BACK')
                                os.system('adb shell input keyevent BACK')
                                os.system('adb shell input keyevent HOME')

doubleC = Camera_pressureTest()
doubleC.getDeava()
# doubleC.EnterExit()
# doubleC.qianEnterExit()
# doubleC.FrontRear()
# doubleC.TakePhoto()
# doubleC.proactive()
# doubleC.xuhuaqiehuanpaizhao()
# doubleC.xuhuapaizhao()
print('test stop ')


