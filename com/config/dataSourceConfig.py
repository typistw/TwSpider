#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
# 配置化
dataSourceConfig = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'123456',
          'db':'scraping',
          'charset':'utf8',
          'cursorclass':pymysql.cursors.DictCursor,
          }