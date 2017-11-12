#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)
from urllib.request import urlopen
from bs4 import  BeautifulSoup
import re
import time
from datetime import datetime
from com.csdn.storage import save

__rootUrl = 'http://blog.csdn.net'

def getOnePageLinks(user, no=1):
    pageLinks=[]
    url = __rootUrl + '/' + user + '/article/list/' + str(no)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    try:
        articleListObj = bsObj.find('div', {'id': 'article_list'})
        # 获取文章链接
        titleLinkLists = articleListObj.findAll('a', href=re.compile('[0-9]$'))
        for link in titleLinkLists:
            if link.attrs['href'] is not None:
                articleUrl = __rootUrl + link.attrs['href']
                if articleUrl not in pageLinks:
                    pageLinks.append(articleUrl)
    except BaseException as e:
        logging.error('get article link error:'+ str(e))

    return pageLinks

def getAllPageLinks(user):
    pageLinks = []
    index = 1
    while index > 0:
        logging.info('index=' + str(index))
        tempPageLinks = getOnePageLinks(user, index)
        if(tempPageLinks is not None and len(tempPageLinks) > 0):
            index += 1
            pageLinks += tempPageLinks
        else:
            index = 0
    return pageLinks

def getTargetData(targetUrl):
    html = urlopen(targetUrl)
    bsObj = BeautifulSoup(html)
    bsInfoObj = bsObj.find('div',{'class':'container clearfix'})
    title = bsInfoObj.find('h1',{'class':'csdn_top'}).text
    original = bsInfoObj.find('div',{'class':'artical_tag'}).find('span',{'class':'original'}).get_text()
    publishDate = bsInfoObj.find('div',{'class':'artical_tag'}).find('span',{'class':'time'}).get_text()
    view = bsInfoObj.find('ul',{'class':'right_bar'}).find('button').get_text()
    tagsObj = bsInfoObj.find('ul',{'class':'article_tags clearfix csdn-tracking-statistics'}).findAll('a')
    tagsList = []
    for value in tagsObj:
        try:
            tagsList.append(value.text)
        except Exception as e:
            logging.error(e)
    tagsStr = ','.join(tagsList)

    content = bsInfoObj.find('div',{'id':'article_content'}).get_text()

    save(title,original, publishDate,view, tagsStr, content)
    # 暂停2s
    time.sleep(2)

if __name__ == '__main__':
    user = 'typist_'
    beginTime = datetime.now()
    logging.info('抓起开始:'+ str(beginTime))
    #获取作者所有文章链接
    pageLinks = getAllPageLinks(user)
    for link in pageLinks:
        getTargetData(link)
    endTime = datetime.now()
    logging.info('抓起结束:'+ str(endTime) + ', 耗时:' + str(endTime - beginTime))
