from django.db import models

# Create your models here.
class product:
    def __init__(self, pid, name, amount, color, size, price):
        self.__name = name
        self.__price = price
        self.__amount = amount
        self.__size = size
        self.__pid = pid
        self.__color = color
        self.__setsum()
        self.__setDelivery()
        self.__setNet()

    def __setsum(self):
        self.__sum = self.__price * self.__amount
    def __setDelivery(self):
        if self.__sum > 1500:
            self.__delivery = 0
        else:
            self.__delivery = 40
    def __setNet(self):
        self.__net = self.__sum + self.__delivery

    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price

    def getPid(self):
        return self.__pid
    def getColor(self):
        return self.__color
    def getSize(self):
        return self.__size
    def getAmount(self):
        return self.__amount
    def getDelivery(self):
        return self.__delivery
    def getNet(self):
        return self.__net
