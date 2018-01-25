from PositionalList import PositionalList
from random import choices
from time import time

def insertion_sort(arr):
    L = arr
    """ Sort PositionalList of comparable elements into nondecreasing order."""
    if len(L) > 1: # otherwise, no need to sort it
        marker = L.first( )
        while marker != L.last( ):
            pivot = L.after(marker) # next item to place
            value = pivot.element( )
            if value > marker.element( ): # pivot is already sorted
                marker = pivot # pivot becomes new marker
            else: # must relocate pivot
                walk = marker # find leftmost item greater than value
                while walk != L.first( ) and L.before(walk).element( ) > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value) # reinsert value before walk

    return L

def insertion_sort2(arr):
    L = arr
    pivot = L.after(L.first())
    while True:
        prev = L.before(pivot)
        if prev.element() < pivot.element():
            new_pivot = L.after(pivot)
        else:
            while (prev.element() > pivot.element()) and prev != L.first():
                prev = L.before(prev)

            if prev.element() > pivot.element():
                L.add_before(prev, pivot.element())
            else:
                L.add_after(prev, pivot.element())

            new_pivot = L.after(pivot)
            L.delete(pivot)

        pivot = new_pivot
        if pivot is None:
            break;

    return L


L = PositionalList()
M = PositionalList()

a = list(range(100000))
new_list = choices(a, k=5000)
while new_list:
    e = new_list.pop()
    L.add_first(e)
    M.add_first(e)



##pos = L.first()
##for i in range(len(L)):
##    print(pos.element())
##    pos = L.after(pos)
##
##print(L.after(L.first()).element())
##

##for e in L:
##    print(e)


t = time()
print(' \n')
insertion_sort(L)
##for e in L:
##    print(e)
print(time() -t)

t = time()
print(' \n')
insertion_sort2(M)
##for e in M:
##    print(e)
print(time() -t)




