##def check_numb(numb):
##    if not (isinstance(numb, float) or isinstance(numb, int)):
##        raise ValueError('price should be a number')
    
class CreditCard:
    """A consumer credit card. """

    def __init__(self, customer, bank, acnt, limit, balance = 0):
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

        try:
            tmp = price + self._balance
        except TypeError:
            return False
        if price < 0:
            raise ValueError("Price should be greater than zero")

        if tmp > self._limit: # if charge would exceed limit,
            return False # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):

        try:
            self._balance -= amount
        except TypeError:
            print('check the number entered')


if __name__ == '__main__':
    wallet = [ ]
    wallet.append(CreditCard( 'John Bowman' , 'California Savings', '5391 0375 9387 5309' , 2500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Federal' , '3485 0399 3395 1954' , 3500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Finance' , '5391 0375 9387 5309' , 5000) )

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print( 'Customer = ', wallet[c].get_customer( ))
        print( 'Bank = ', wallet[c].get_bank())
        print( 'Account = ', wallet[c].get_account( ))
        print( 'Limit = ', wallet[c].get_limit( ))
        print( 'Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance( ) > 100:
            wallet[c].make_payment(100)
            print( 'New balance = ', wallet[c].get_balance())
        print( )
