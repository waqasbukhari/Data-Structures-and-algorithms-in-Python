from creditcardclass import CreditCard

class PredatoryCreditCard(CreditCard):
    def __init__(self,customer,bank,acnt,limit,apr):

        super().__init__(customer,bank,acnt,limit)
        self._apr = apr

    def charge(self,price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success
    def process_month(self):

        if self._balance > 0:

            monthly_factor = pow(1+sel._apr,1/2)
            self._balance *= monthly_factor



