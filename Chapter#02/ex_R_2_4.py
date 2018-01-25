#!/usr/bin/env python3

class Flower:
    def __init__(self, name, numb_petals, price):
        self._name = name
        self._numb_petals = numb_petals
        self._price = price

    def set_name(self, name):
        self._name = name
    def set_numb_petals(self, numb_petals):
        self._numb_petals = numb_petals
    def set_price(self, price):
        self._price = price
        
        
    def get_name(self):
        return self._name
    
    def get_numb_petals(self):
        return self._numb_petals
    
    def get_price(self):
        return self._price

    def describe(self):
        return "This flower is named {}, has {} number of petals and its price is {} ".format(self._name, self._numb_petals, self._price)

if __name__ == '__main__':
    rose = Flower('Rose', 10, 5)
    print(rose.get_name())
    print(rose.describe())
        
        
