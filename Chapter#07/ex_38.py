from PosList import PositionalList

import random
PL = PositionalList()

for i in range(20):
    PL.add_first(random.randint(0,1500))

def bubble_sort(PL):
    cursor1 = PL.first()
    cursor2 = PL.after(cursor1)
    while cursor1 is not None:
        cursor2 = PL.first()
        while cursor2 is not None:
            if cursor1.element() > cursor2.element():
                PL.swap(cursor1,cursor2)
            cursor2 = cursor2.after()
        cursor1 = cursor1.after
        


sorted_list = bubble_sort(PL)
    
