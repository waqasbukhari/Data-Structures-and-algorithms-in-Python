from creditcardclass import CreditCard

class PredatoryCreditCard(CreditCard):
    def __init__(self,customer,bank,acnt,limit,apr):

        super().__init__(customer,bank,acnt,limit)
        self._apr = apr

    def charge(self,price,times_monthly_charge):
        success = super().charge(price)

        if times_monthly_charge <= 10:
            
            if not success:
                self._balance += 5
        else:
            if not success:
                self._balance += 6
        return success
        
    def process_month(self):

        if self._balance > 0:

            monthly_factor = pow(1+sel._apr,1/2)
            self._balance *= monthly_factor



