#!/usr/bin/env python3
# -*- coding: utf-8 -*-

station_coding_map = {}

def init_station_coding_map():
    global  station_coding_map
    f = None
    try:
        f = open('stationCoding.txt', encoding='utf-8')
        codingInfo = f.read()
        for item in codingInfo.split('@'):
            if item:
                coding_list = item.split('|')
                # 提取站点 中文名称[1]与编码[2]
                station_coding_map[coding_list[1]] = coding_list[2]
    except Exception as  e:
        print("open stationCoding.txt failed:", e)
    finally:
        if f is not None:
            f.close()