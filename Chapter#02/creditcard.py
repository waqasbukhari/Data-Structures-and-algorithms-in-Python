class CreditCard:
    def __init__ (self,customer,bank, acnt,limit,balance):
        
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._get_balance = balance #R07
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_acnt(self):
        return self._acnt
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._get_balance

    def charge(self,price):
        #R05
        try:
            price = int(price)
        except:
            TypeError('charge only accepts integer values')
        
        if price + self._balance > self.limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self,amount):
        #R06

        if amount <=0:
            raise ValueError('payment cannot be negative')
        #R05
        try:
            price = int(price)
        except:
            TypeError('charge only accepts integer values')

        self._balance -= amount

    #R29    
    def _set_balance(b):
        self.get_balance = b
