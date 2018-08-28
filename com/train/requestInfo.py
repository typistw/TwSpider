#!/usr/bin/env python3
# -*- coding: utf-8 -*-

phantomjs_path = 'D:\\phantomJs\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'

head = {
    'Host': 'www.12306.cn',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Cookie': 'RAIL_EXPIRATION=1516778732279; RAIL_DEVICEID=p300DPGtqYmxVnQJ0wLgLBXw0QURfmTh2QTB5mHmf9VK0JCC6UqXjbZCgjQ6adKOAcyU58EXb6AP07KsV5TPkJ6KaWJwuTC8CSCHM3ki1I-rkwUfcmTB5rqNgWYn6HMnw_bR583VetHCh5ssJKzETglmtTPUPTOf; _jc_save_fromStation=%u5A01%u820D%2CWSM; _jc_save_toStation=%u8D35%u9633%2CGIW; _jc_save_fromDate=2018-02-20; _jc_save_toDate=2018-01-23; _jc_save_wfdc_flag=dc'
}
proxies = {'http': 'http://218.56.132.156:8080'}