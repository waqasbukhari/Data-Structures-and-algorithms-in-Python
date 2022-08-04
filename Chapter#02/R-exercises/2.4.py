class flower:
    def __init__ (self,name,num_petals,price):
        self._name = name
        self._num_petals = num_petals
        self._price = price
    def get_name(self):
        return self._name
    def get_num_petals(self):
        return self._num_petals
    def get_price(self):
        return self._price
s = flower(name = 'rose',num_petals = 10,price = 50)
name = s.get_name()
print(name)
