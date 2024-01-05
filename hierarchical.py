class Parent:
    def __init__(self,house,land):
        self.house=house
        self.land=land
class child1(parent):
    def __init__(self,house,land,car,cash):
         super().__init__(house,land)
         self.car=car
         self.cash=cash
class child2(parent):
    pass
c1=child