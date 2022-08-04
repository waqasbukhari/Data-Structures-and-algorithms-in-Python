class CreditCard:
    def __init__ (self,customer,bank, acnt,limit):
        
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_acnt(self):
        return self._acnt
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance

    def charge(self,price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self,amount):

        self._balance -= amount
        
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('A','X','111',1200))
    wallet.append(CreditCard('B','Y','222',3500))
    wallet.append(CreditCard('C','Z','111',5000))
    for val in range(1,2500):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    for c in range(3):
        print('customer = ',wallet[c].get_customer())
        print('bank = ',wallet[c].get_bank())
        print('Account = ',wallet[c].get_acnt())
        print('Limit = ',wallet[c].get_limit())
        print('Balance = ',wallet[c].get_balance)
        while wallet[c].get_balance()>100:
            wallet[c].make_payment(100)
            print('new_balance = ',wallet[c].get_balance())
        print()
