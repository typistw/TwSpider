#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
from com.train.trainInfo import trainBaseInfo
import time, requests, json



phantomjs_path = 'D:\phantomJs\phantomjs-2.1.1-windows\\bin\phantomjs.exe'

head = {
    'Host': 'www.12306.cn',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
proxies = {'http': 'http://218.56.132.156:8080'}

def dynamic_page_load(url):
    driver = webdriver.PhantomJS(executable_path=phantomjs_path)
    driver.set_page_load_timeout(20)
    driver.set_script_timeout(20)
    pageSource = None
    try:
        driver.get(url)
        time.sleep(2)
        pageSource = driver.page_source
    except Exception as e:
        print(" request url error : ", url )
    finally:
        driver.close()
    return  pageSource

def get_train_number_list(url):
    pageSource = dynamic_page_load(url)
    if(pageSource is not None):
        bsObj = BeautifulSoup(pageSource)
        json_str_info = bsObj.find('html').get_text()

        json_obj_info = json.loads(json_str_info)
        # 获取整个数据节点
        data_info = json_obj_info['data']
        # 获取查询数据
        result_obj = data_info['result']
        return result_obj
    else:
        return None

def get_need_data_map(url):
    result_list = get_train_number_list(url)
    train_info_map = {}
    if(result_list is not None):
        for value in result_list:
            index = 0
            trainInfo = trainBaseInfo()
            info_map = {}
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

# def get

if __name__ == '__main__':
    # 火车全国站点对应编码
    # https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9002

    # 参考
    # https://www.cnblogs.com/qwangxiao/p/7199870.html

    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-09&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=GIW&purpose_codes=ADULT'
    data_map = get_need_data_map(url)

    # print(json.dumps(data_map,ensure_ascii=False))
    print(json.dumps(data_map, default=lambda obj: obj.__dict__, indent=4, ensure_ascii=False))
