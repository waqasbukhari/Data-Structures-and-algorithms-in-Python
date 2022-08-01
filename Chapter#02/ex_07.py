#!/usr/bin/env python3

"""
Code is added in method of __init__() of the CreditCard class. 
The changes are enclosed within comments specifying it to be part of R-2.7.
"""

from CreditCard import CreditCard

# Optional parameter balance with default value of 0. 
card1 = CreditCard('John Doe', '1st Bank' , '5391 0375 9387 5309 ', 1000) 
print(card1.get_balance())
# balance is initialized to 50000
card2 = CreditCard('John Doe', '1st Bank' , '5391 0375 9387 5309 ', 1000, 50000) 
print(card2.get_balance())
