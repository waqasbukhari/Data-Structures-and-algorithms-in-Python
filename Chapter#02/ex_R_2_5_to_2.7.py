class CreditCard:
    """A consumer credit card. """

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """ Create a new credit card instance.
            The initial balance is zero.
            customer the name of the customer (e.g., John Bowman )
            bank the name of the bank (e.g., California Savings )
            acnt the acount identifier (e.g., 5391 0375 9387 5309 )
            limit credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        if not ((isinstance(float(price), float)) and (price > 0)):
            raise ValueError('price should be a positive real number')
        
            
        if price + self._balance > self._limit: # if charge would exceed limit,
            return False # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if not ((isinstance(float(amount), float)) and (amount > 0)):
            raise ValueError('amount should be a positive real number')
        self._balance -= amount



if __name__ == '__main__':
    cc = CreditCard('John Doe', '1st Bank' , '5391 0375 9387 5309 ', 1000)
    cc.charge(100.0)
    cc.make_payment(-10)
