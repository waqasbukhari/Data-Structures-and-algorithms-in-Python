#!/usr/bin/env python3
import os
os.chdir('C:\\Users\\super\\Desktop\\Preparing for Programming\\Exercise - Data Structures and Algorithms in Python\\Chapter#01')
from ex_R_1_2 import is_even
import time
def odd_product(int_seq):
    
    """ Given a sequence of numbers, find a pair of unique numbers
    whose product is odd  """
    for i in range(len(int_seq)):
        for j in range(i+1, len(int_seq)):
            numb_a = int_seq[i]
            numb_b = int_seq[j]

            if numb_a != numb_b:
                product = numb_a * numb_b
                if not is_even(product):
                    print(numb_a, numb_b)

def odd_product_2(int_seq):
    
    """ Given a sequence of numbers, find a pair of unique numbers
    whose product is odd  """

    ## Exploiting the fact: odd number multiplied by odd number yields an odd number.
    new_seq = [numb for numb in int_seq if not is_even(numb)]
    
    for i in range(len(new_seq)):
        for j in range(i+1, len(new_seq)):
            numb_a = new_seq[i]
            numb_b = new_seq[j]

            if numb_a != numb_b:
                product = numb_a * numb_b
                if not is_even(product):
                    print(numb_a, numb_b)

def odd_product_3(int_seq):
    
    """ Given a sequence of numbers, find a pair of unique numbers
    whose product is odd  and using list comprehensions"""

    ## Exploiting the fact: odd number multiplied by odd number yields an odd number.
    new_seq = [numb for numb in int_seq if not is_even(numb)]
    
    
    for i in range(len(new_seq)):
        range_j = list(range(i+1, len(new_seq)))
        range_i = [i] * len(range_j)
        [new_seq[i], new_seq[j] for i,j in zip(range_i, range_j) if (new_seq[i] != new_seq[j]) and (not is_even(new_seq[i] * new_seq[j]))]

if __name__ == '__main__':

    lst_numbers = list(range(10))
    t1 = time.time()
    odd_product(lst_numbers)
    print(time.time() - t1)

    
    t2 = time.time()
    odd_product_2(lst_numbers)
    print(time.time() - t2)
    
    t3 = time.time()
    odd_product_3(lst_numbers)
    print(time.time() - t3)
    
