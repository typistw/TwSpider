#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from bs4 import BeautifulSoup
from com.train.trainInfo import trainBaseInfo
from com.train.requestInfo import *
from  datetime import datetime
import json, time

PROXY = '218.56.132.156:8080'

phantom_proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': PROXY,
    'ftpProxy': PROXY,
    'sslProxy': PROXY,
    'noProxy': False # set this value as desired
    })

def dynamic_page_load(url):
    desired_capabilities =  webdriver.DesiredCapabilities.PHANTOMJS.copy()

    # 添加代理
    # phantom_proxy.add_to_capabilities(desired_capabilities)

    for key, value in head.items():
        desired_capabilities['phantomjs.page.settings.{}'.format(key)] = value

    driver = webdriver.PhantomJS(
        executable_path=phantomjs_path,
        desired_capabilities=desired_capabilities
    )
    pageSource = None
    try:
        driver.get(url)
        print(datetime.now())
        # 构成隐式等待, 10s内若有则立即返回, 否则会抛出 TimeoutException
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'someId')))
        # 显示等待
        time.sleep(3)
        print(datetime.now())
        pageSource =  driver.page_source
    except Exception as e:
        print(" request error : ", e )
    finally:
        driver.close()
    return  pageSource

def get_train_number_list(url):
    pageSource = dynamic_page_load(url)
    if(pageSource is not None):
        try:
            bsObj = BeautifulSoup(pageSource)
            json_str_info = bsObj.find('html').get_text()

            json_obj_info = json.loads(json_str_info)
            # 获取整个数据节点
            data_info = json_obj_info['data']
            # 获取查询数据
            result_obj = data_info['result']
            return result_obj
        except :
            print('the query has not data!')
            return None
    else:
        return None

def get_need_data_map(url):
    result_list = get_train_number_list(url)
    train_info_map = {}
    if(result_list is not None):
        for value in result_list:
            index = 0
            trainInfo = trainBaseInfo()
            trainNumber = None
            for item in value.split('|'):
                # 1 余票状态
                if(index == 1):
                    trainInfo.trainStatus = item
                # 3 车次
                elif(index == 3):
                    trainInfo.trainNumber = item
                    trainNumber = item
                # 6 出发地代码
                elif(index == 6):
                    trainInfo.startPlaceCode = item
                # 7 目的地代码
                elif(index == 7):
                    trainInfo.destinationCode = item
                # 8 发车时间
                elif(index == 8):
                    trainInfo.startTime = item
                # 9 到达时间
                elif(index == 9):
                    trainInfo.endTime = item
                # 10 运行时长
                elif(index == 10):
                    trainInfo.usedTime = item
                # 11 是否可购买
                elif(index == 11):
                    trainInfo.canWebBuy = item
                # 13 乘车日期
                elif(index == 13):
                    trainInfo.toDate = item
                # 23 软卧
                elif(index == 23):
                    trainInfo.softSleeper = item
                # 24 软座
                elif(index == 24):
                    trainInfo.softSeat = item
                # 26 无座
                elif(index == 26):
                    trainInfo.withoutSeat = item
                # 28 硬卧
                elif(index == 28):
                    trainInfo.hardSleeper = item
                # 29 硬座
                elif(index == 29):
                    trainInfo.hardSeat = item
                # 30 二等座
                elif(index == 30):
                    trainInfo.secondClassSeat = item
                # 31 一等座
                elif(index == 31):
                    trainInfo.firsClassSeat = item
                # 32 商务座/特等座
                elif(index == 32):
                    trainInfo.principalSeat = item
                # 33 动卧
                elif(index == 33):
                    trainInfo.EMUSleeper = item
                index += 1
            train_info_map[trainNumber] = trainInfo
    return train_info_map

if __name__ == '__main__':
    testUrl = 'http://httpbin.org/ip'
    print(dynamic_page_load(testUrl))