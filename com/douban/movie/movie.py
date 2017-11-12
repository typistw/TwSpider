#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)
from selenium import webdriver
import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from com.douban.movie.movieInfo import movieInfo
from com.douban.movie.persistentService import insertMovieInfo, insertMovieBaseInfo
import json
import queue

# 分类排行榜枚举
movieType = {11: '剧情', 24: '喜剧', 5: '动作', 13: '爱情', 17: '科幻', 25: '动画', 10: '悬疑', 19: '惊悚', 20: '恐怖', 1: '纪录片',
             23: '短片', 6: '色情', 26: '同性',14: '音乐', 7: '歌舞', 28: '家庭', 8: '儿童', 2: '传记', 4: '历史', 22: '战争', 3: '犯罪',
             27: '西部', 16: '奇幻', 15: '冒险',12: '灾难', 29: '武侠', 30: '古装', 18: '运动', 31: '黑色电影'}

# 分类排行前百分之50
rankGrade = {100:90, 90:80, 80:70, 70:60, 60:50}

phantomjs_path = 'D:\phantomJs\phantomjs-2.1.1-windows\\bin\phantomjs.exe'

head = {
    'Host': 'movie.douban.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
# 西刺代理[http://www.xicidaili.com/]
proxies = {'https': 'http://218.56.132.156:8080'}

def dynamic_load(url):
    driver = webdriver.PhantomJS(
        executable_path=phantomjs_path
    )
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    pageSource = None
    try:
        driver.get(url)
        #等待脚本执行3秒
        time.sleep(3)
        pageSource = driver.page_source
    except Exception as e:
        logging.error('get request error' + str(e))
    finally:
        driver.close()
    return pageSource

def getMovieInfoLinks(url):
    pageSource = dynamic_load(url)
    movieLinkList = []
    if(pageSource is not None):
        bsObj = BeautifulSoup(pageSource)
        movieListA = bsObj.find('div',{'class':'movie-list-panel pictext'}).findAll('a')
        for obj in movieListA:
            try:
                link= obj.attrs['href']
                if(link not in movieLinkList):
                    movieLinkList.append(link)
            except Exception as e:
                logging.error('not tag a:' + str(e))
    else:
        logging.info('no data url: ' + url)
    return movieLinkList

def getContentValue(value):
     values = value.split(':')
     return values[1:]

def getMovieBaseInfo(movieLinks, movieType):
    if(movieLinks is not None):
        for link in movieLinks:
            try:
                html = requests.get(link, headers=head, timeout=30, proxies=proxies)
                bsObj = BeautifulSoup(html.content)
                name = bsObj.find('h1').find('span').get_text()
                grade = bsObj.find('div',{'class':'rating_self clearfix'}).find('strong').get_text()

                info = movieInfo()
                info.type = movieType
                info.movieName = name
                info.grade = grade

                movieInfoObj = bsObj.find('div', {'id':'info'})
                movie = movieInfoObj.get_text()
                movie = movie.split('\n')
                index = 1
                for item in movie:
                    if(index == 2):
                        director = getContentValue(item)
                        info.director = director
                    if(index == 3):
                        scriptwriter = getContentValue(item)
                        info.scriptwriter = scriptwriter
                    if(index == 4):
                        actor = getContentValue(item)
                        info.actor = actor
                    if(index == 6):
                        area = getContentValue(item)
                        info.area = area
                    if(index == 7):
                        language = getContentValue(item)
                        info.language = language
                    if(index == 8):
                        releaseDate = getContentValue(item)
                        info.releaseDate = releaseDate
                    if(index == 9):
                        filmTime = getContentValue(item)
                        info.filmTime = filmTime
                    index += 1

                #  data storage
                insertMovieInfo(info)
                logging.info(link + ' 抓起完毕')
            except Exception as e:
                logging.error(' url error:' + link + ', '+ str(e))

def oldMethod():
    # 抓起分类排行榜前50%的电影信息
    for key, typeName in movieType.items():
        # 分类排行前50%
        typeLinks = []
        for high, low in rankGrade.items():
            #只能获取前20条数据
            url = 'https://movie.douban.com/typerank?type_name=' + str(typeName) + '&type=' + str(key) +\
                  '&interval_id=' + str(high) + ':' +  str(low) +'&action='
            links = getMovieInfoLinks(url)
            typeLinks += links
        logging.info('获取 '+ str(typeName) + ' 类型url完毕')
        getMovieBaseInfo(typeLinks, typeName)

def execute(url):
    try:
        re = requests.get(url, headers=head, timeout=30, proxies=proxies)
        jsonList = json.loads(re.text)
        re.close()
        for obj in jsonList:
            insertMovieBaseInfo(obj)
        logging.info(url + ' 抓起完毕')
        return True
    except Exception as e:
        logging.error(str(e) + ', url:' + url)
        return False

def newMethod():
    failedQueue = queue.Queue()
    # 31种分类
    for x in range(1,32):
        for high, low in rankGrade.items():
            url = 'https://movie.douban.com/j/chart/top_list?type=' + str(x) + '&interval_id=' + str(high) + ':' + str(low) + '&action=&start=0&limit=1000'
            if(execute(url) == False):
                failedQueue.put(url)
            time.sleep(1)

    # 失败url重试
    while not failedQueue.empty():
        url = failedQueue.get()
        if(execute(url) == False):
            failedQueue.put(url)
        time.sleep(1)

if __name__ == '__main__':
    begin = datetime.now()
    logging.info('抓起开始:' + str(begin))
    newMethod()
    end = datetime.now()
    logging.info('抓起结束:' + str(end) + ', 耗时:' + str(end - begin))