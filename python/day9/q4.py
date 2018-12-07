#!/usr/bin/python
class vehicle:
    def __init__(self,nameofowner,vehno,noofwheels,yearofmake,buyingprice):
        self.owner=nameofowner
        self.vehno=vehno
        self.wheels=noofwheels
        self.year=yearofmake
        self.price=buyingprice
        self.cy = 2018
        self.gap = self.cy - self.year
    def show(self):
        print'owner',self.owner
        print'vehicle no',self.vehno
        print'wheels',self.wheels
        print'year',self.year
        print'price',self.price
    def calc(self):
        pass

class car(vehicle):

    def calc(self):
        value = self.price-(5000*self.gap)
        print 'the market value is: ',value
       
class bus(vehicle):

    def calc(self):
        value = self.price-(1000*self.gap)
        print 'the market value is: ',value

class truck(vehicle):

    def calc(self):
        value = self.price-(12000*self.gap)
        print 'the market value is: ',value

car = car("paramesh",2420,4,2008,260000)
car.show()
car.calc()

bus = bus("hareesh",4202,8,2008,10000)
bus.show()
bus.calc()

truck= truck("mareesh",1420,10,2016,260000)
truck.show()
truck.calc()
