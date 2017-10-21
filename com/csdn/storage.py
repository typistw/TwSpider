#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import logging; logging.basicConfig(level=logging.INFO)

# 配置化
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'123456',
          'db':'scraping',
          'charset':'utf8',
          'cursorclass':pymysql.cursors.DictCursor,
          }

#获取连接
connection = pymysql.connect(**config)

def save(title, original, publishDate, view, tagsStr, content):
    cursor = connection.cursor()
    try:
        sql = 'INSERT INTO csdnblog (title,copyright,date,view,tags,content) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(sql,(title, original, publishDate, view, tagsStr, content))
        connection.commit()
    except Exception as e:
        logging.error('execute sql',e)
    finally:
        cursor.close()
