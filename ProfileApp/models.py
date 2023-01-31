from django.db import models

# Create your models here.
class product:
    def __init__(self, pid, name, scale, tier, height, price, image):
        self.__name = name
        self.__price = price
        self.__image = image
        self.__scale = scale
        self.__height = height
        self.__pid = pid
        self.__tier = tier
        self.__setDiscount()
        self.__setsum()
        self.__setDelivery()
        self.__setNet()
    def __setDiscount(self):
       if self.__price > 2500:
            self.__discount = self.__price * 0.1
       elif self.__price > 2000:
           self.__discount = self.__price * 0.05
       elif self.__price > 1500:
           self.__discount =  self.__price * 0.03
       else:
           self.__discount = 0
    def __setsum(self):
        self.__sum = self.__price - self.__discount
    def __setDelivery(self):
        if self.__sum > 2000:
            self.__delivery = 0
        else:
            self.__delivery = 75
    def __setNet(self):
        self.__net = self.__sum + self.__delivery

    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    def getImage(self):
        return self.__image
    def getPid(self):
        return self.__pid
    def getTier(self):
        return self.__tier
    def getHeight(self):
        return self.__height
    def getScale(self):
        return self.__scale
    def getDiscount(self):
        return self.__discount
    def getDelivery(self):
        return self.__delivery
    def getNet(self):
        return self.__net
