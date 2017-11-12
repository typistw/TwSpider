#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import logging; logging.basicConfig(level=logging.INFO)
from com.config.dataSourceConfig import dataSourceConfig

#获取连接
connection = pymysql.connect(**dataSourceConfig)

def save(title, original, publishDate, view, tagsStr, content):
    cursor = connection.cursor()
    try:
        sql = 'INSERT INTO csdnblog (title,copyright,date,view,tags,content) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(sql,(title, original, publishDate, view, tagsStr, content))
        connection.commit()
    except Exception as e:
        logging.error('execute sql'+ str(e))
    finally:
        cursor.close()
