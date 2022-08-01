#!/usr/bin/env python3

"""
Code is added in methods of charge() and make_payment() of the CreditCard class. 
The changes are enclosed within comments specifying it to be part of R-2.5.
"""

from CreditCard import CreditCard

card = CreditCard('John Doe', '1st Bank' , '5391 0375 9387 5309 ', 1000)
card.charge(100)
card.make_payment(10)

card.make_payment('strange') # exception ValueError is thrown. 
