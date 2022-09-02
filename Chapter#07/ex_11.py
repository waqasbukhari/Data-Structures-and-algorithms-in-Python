from PosList import PositionalList

PL = PositionalList()

for i in range(10,1,-1):
    PL._insert_between(i,PL._header,PL._trailer)
#print(PL._element)

def max_ele(PL):
        max_element = 0
        for x in PL:
            if x > max_element:
                max_element = x
        print(max_element)
        return max_element
max_element = max_ele(PL)
