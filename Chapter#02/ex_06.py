#!/usr/bin/env python3

"""
Code is added in method of make_payment() of the CreditCard class. 
The changes are enclosed within comments specifying it to be part of R-2.6.
"""

from CreditCard import CreditCard


card = CreditCard('John Doe', '1st Bank' , '5391 0375 9387 5309 ', 1000)
card.make_payment(10)
card.make_payment(-10) # exception ValueError is raised. 
