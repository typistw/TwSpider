#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import logging; logging.basicConfig(level=logging.INFO)
from com.config.dataSourceConfig import dataSourceConfig

connection = pymysql.connect(**dataSourceConfig)

def insertMovieInfo(movieInfo):
    cursor = connection.cursor()
    try:
        sql = 'insert into douban_movie (name, grade, director, scriptwriter, actor, area, language, releaseDate, filmTime, type)' \
              ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(sql,(movieInfo.movieName, movieInfo.grade, movieInfo.director, movieInfo.scriptwriter, movieInfo.actor, movieInfo.area
                            , movieInfo.language, movieInfo.releaseDate, movieInfo.filmTime, movieInfo.type))
        connection.commit()
    except Exception as e:
        logging.error('execute sql error:' + str(e))
    finally:
        cursor.close()

def insertMovieBaseInfo(jsonMovie):
    cursor = connection.cursor()
    try:
        sql = 'insert into douban_movie_two (name, score, regions, release_date, vote_count, types, actors)' \
              ' VALUES (%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, (jsonMovie['title'], jsonMovie['score'], str(jsonMovie['regions']), jsonMovie['release_date'],
                             jsonMovie['vote_count'], str(jsonMovie['types']), str(jsonMovie['actors']) ))
        connection.commit()
    except Exception as e:
        logging.error('execute sql error:' + str(e) + '\n' + 'insert error data:' + str(jsonMovie))
    finally:
        cursor.close()