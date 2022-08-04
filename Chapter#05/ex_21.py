#!/usr/bin/env python3
from time import time

def time_method(method, document):
    REPETITIONS = 20
    t = time()
    for _ in range(REPETITIONS):
        method(document)

    return (time() - t) / REPETITIONS

def concat(document):
    letters = ''
    for c in document:
        if c.isalpha():
            letters += c
    return c

def list_join(document):
    letters = []
    for c in document:
        if c.isalpha():
            letters.append(c)
    return ''.join(letters)

def list_compr_join(document):
    return ''.join([c for c in document if c.isalpha()])


def gen_compr_join(document):
    return ''.join((c for c in document if c.isalpha()))



def string_methods(): 
    with open('test.txt','r') as f:
        data = f.read()

    for method in ['concat', 'list_join', 'list_compr_join', 'gen_compr_join']:
        time = time_method(eval(method), data)
        print('{} method time is {:e}'.format(method, time))

if __name__ == "__main__":
    string_methods()