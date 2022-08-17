from LinkedStack import LinkedStack

def second_last(L):
    """
    Tail's next is None. 
    if an eleemnt's next is not None, it can be tail. 
    so, we have an element whose next's next is a tail then its 
    next is second to tail. 
    """
    # starting off from head. we assume it is second to tail. 
    e = L._head 
    # When the condition fails, e is second to last, with e._next is the tail and e._next._next is None. 
    while e._next._next is not None: 
        e = e._next

    return e._element


# defining and populating a linked list. 
L = LinkedStack()
for i in range(10):
    L.push(i)

print(second_last(L))