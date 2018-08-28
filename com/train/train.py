#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, requests, json
from com.train.queryTicket import get_need_data_map
from com.train.stationCodingMap import *
from com.train.requestInfo import *

# 火车全国站点对应编码
# https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9002

def get_bus_information():
    while True:
        start_place = input('出发地 [格式:北京]:')
        if start_place in station_coding_map:
            start_place = station_coding_map.get(start_place)
            break
        else:
            print('出发地车站不存在,请重新输入!')
            continue
    while True:
        destination = input('目的地 [格式:天津]:')
        if destination in station_coding_map:
            destination = station_coding_map.get(destination)
            break
        else:
            print('目的地车站不存在,请重新输入!')
            continue
    while True:
        to_date = input("出发日期 [格式: 2018-02-09]:")
        try:
            time.strptime(to_date,'%Y-%m-%d')
            break
        except:
            print('日期格式或时间非法,请重新输入!')
    return start_place, destination, to_date

# 参考
# https://www.cnblogs.com/qwangxiao/p/7199870.html
if __name__ == '__main__':
    init_station_coding_map()

    start_place, destination, to_date = get_bus_information()
    query_url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?' \
                'leftTicketDTO.train_date=' + to_date +'&leftTicketDTO.from_station=' + start_place + \
                '&leftTicketDTO.to_station=' + destination + '&purpose_codes=ADULT'

    data_map = get_need_data_map(query_url)
    print(json.dumps(data_map, default=lambda obj: obj.__dict__, indent=4, ensure_ascii=False))
    print('==============================')