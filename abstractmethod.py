from abc import ABC abstractmethod

class car(abc):
    def__init__(self,name,color,price):
    self.name=name
    self.color=color
    self.price=price
    self.speed=0


@abstractmethod
def stop():
    pass
@abstractmethod
def speed_up(self):
    pass
@abstractmethod
def speed_down():
    pass
class Bmw(car):
    def speed_up(self):
        self.speed+=5
    def speed_down(self):
        self.speed-=5
    def stop(self):
        self.speed=0
class Tata(car):
    def speed_up(self):
        self.speed+=2
    def speed_down(self):
        self.speed-=2
    def stop(self):
        self.speed=0




