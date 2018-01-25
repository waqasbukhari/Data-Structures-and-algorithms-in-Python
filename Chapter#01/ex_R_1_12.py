#!/usr/bin/env python3

def our_choice(seq):
    import random
    idx = random.randrange(len(seq))
    return seq[idx]


if __name__ == '__main__':
    sequence = list(range(20))
    print(our_choice(sequence))
