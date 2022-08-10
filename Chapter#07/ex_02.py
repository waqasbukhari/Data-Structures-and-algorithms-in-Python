from LinkedStack import LinkedStack

def concat_lists(L1, L2):
    """
    Tail's next is None. 
    if an eleemnt's next is not None, it can be tail. 
    so, we have an element whose next's next is a tail then its 
    next is second to tail. 
    """
    # starting off from head. we assume it is second to tail. 
    e1 = L1._head
    e2 = L2._head
    # assume list sizes are not available. 

    while e1._next is not None: # on failing e1 would be tail to L1
        e1 = e1._next

    # making tail of L1's next to the head of L2. 
    e1._next = e2 

    return L1._head

def print_list(node):
    "given head of a list, print all elements. "
    while node._next is not None:
        print(node._element)
        node = node._next
    


# defining and populating a linked list. 
L1 = LinkedStack()
for i in range(10):
    L1.push(i)

L2 = LinkedStack()
for i in range(10,20):
    L2.push(i)

node = concat_lists(L1,L2)
print_list(node)