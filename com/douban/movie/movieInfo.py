#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class movieInfo(object):

    @property
    def movieName(self):
        return self.__movieName

    @movieName.setter
    def movieName(self, name):
        self.__movieName = name

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        self.__director = director

    @property
    def scriptwriter(self):
        return self.__scriptwriter

    @scriptwriter.setter
    def scriptwriter(self, scriptwriter):
        self.__scriptwriter = scriptwriter

    @property
    def actor(self):
        return self.__actor

    @actor.setter
    def actor(self, actor):
        self.__actor = actor

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        self.__language = language

    @property
    def releaseDate(self):
        return self.__releaseDate

    @releaseDate.setter
    def releaseDate(self, releaseDate):
        self.__releaseDate = releaseDate

    @property
    def filmTime(self):
        return self.__filmTime

    @filmTime.setter
    def filmTime(self, filmTime):
        self.__filmTime = filmTime

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, filmTime):
        self.__type = filmTime