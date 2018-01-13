#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class trainBaseInfo:

    @property
    def trainStatus(self):
        return self.__trainStatus

    @trainStatus.setter
    def trainStatus(self, status):
        self.__trainStatus = status

    @property
    def trainNumber(self):
        return self.__trainNumber

    @trainNumber.setter
    def trainNumber(self, trainNumber):
        self.__trainNumber = trainNumber

    @property
    def startPlaceCode(self):
        return self.__startPlaceCode

    @startPlaceCode.setter
    def startPlaceCode(self, startPlaceCode):
        self.__startPlaceCode = startPlaceCode

    @property
    def destinationCode(self):
        return self.__destinationCode

    @destinationCode.setter
    def destinationCode(self, destinationCode):
        self.__destinationCode = destinationCode

    @property
    def startTime(self):
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime):
        self.__startTime = startTime

    @property
    def endTime(self):
        return self.__endTime

    @endTime.setter
    def endTime(self, endTime):
        self.__endTime = endTime

    @property
    def usedTime(self):
        return self.__usedTime

    @usedTime.setter
    def usedTime(self, usedTime):
        self.__usedTime = usedTime

    @property
    def canWebBuy(self):
        return self.__canWebBuy

    @canWebBuy.setter
    def canWebBuy(self, canWebBuy):
        self.__canWebBuy = canWebBuy

    @property
    def toDate(self):
        return self.__toDate

    @toDate.setter
    def toDate(self, toDate):
        self.__toDate = toDate

    @property
    def softSleeper(self):
        return self.__softSleeper

    @softSleeper.setter
    def softSleeper(self, softSleeper):
        self.__softSleeper = softSleeper

    @property
    def softSeat(self):
        return self.__softSeat

    @softSeat.setter
    def softSeat(self, softSeat):
        self.__softSeat = softSeat

    @property
    def hardSeat(self):
        return self.__hardSeat

    @hardSeat.setter
    def hardSeat(self, hardSeat):
        self.__hardSeat = hardSeat

    @property
    def hardSleeper(self):
        return self.__hardSleeper

    @hardSleeper.setter
    def hardSleeper(self, hardSleeper):
        self.__hardSleeper = hardSleeper

    @property
    def withoutSeat(self):
        return self.__withoutSeat

    @withoutSeat.setter
    def withoutSeat(self, withoutSeat):
        self.__withoutSeat = withoutSeat

    @property
    def firsClassSeat(self):
        return self.__firsClassSeat

    @firsClassSeat.setter
    def firsClassSeat(self, firsClassSeat):
        self.__firsClassSeat = firsClassSeat

    @property
    def secondClassSeat(self):
        return self.__secondClassSeat

    @secondClassSeat.setter
    def secondClassSeat(self, secondClassSeat):
        self.__secondClassSeat = secondClassSeat

    @property
    def principalSeat(self):
        return self.__principalSeat

    @principalSeat.setter
    def principalSeat(self, principalSeat):
        self.__principalSeat = principalSeat

    @property
    def EMUSleeper(self):
        return self.__EMUSleeper

    @EMUSleeper.setter
    def EMUSleeper(self, EMUSleeper):
        self.__EMUSleeper = EMUSleeper