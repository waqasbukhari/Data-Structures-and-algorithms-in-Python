class CreditCard:
    def __init__ (self,customer,bank, acnt,limit):
        
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._get_balance = 0
        
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
        try:
            price = int(price)
        except:
            TypeError: "charge only accepts integer valuess"
        if price + self._balance > self.limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self,amount):
        try:
            amount = int(amount)
        except:
            TypeError: "enter integer valuess for payment"

        self._balance -= amount
        
