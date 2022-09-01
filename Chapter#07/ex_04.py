from LinkStack import LinkedStack
from  DoublyLinkedList import _DoublyLinkedBase
#from DoublyLinkedList import DoublyLinkedBase

#swaping nodes with singly linked list


L = LinkedStack()
for i in range(10):
    L.push(i)



def swapsingle(L):
    head_old = L._head
    head_old_ele = L._head._element
    head_new = L._head._next
    head_new_ele = L._head._next._element
    L._head._next = L._Node(head_old_ele,head_old)
    L._head = L._Node(head_new_ele,head_new)
    
    return L


L = swapsingle(L)
print(L._head._element)


L = _DoublyLinkedBase()
for i in range(10):
    L._insert_between(i, L._header,L._trailer)

    
def swapdouble(L,node1,node2):
    node1_old_prev = node1._prev
    node1_old_next = node1._next
    node1_old_element = node1._element

    node2_old_prev = node2._prev
    node2_old_next = node2._next
    node2_old_element = node2._element

    L._node1._next = node2_old_next
    L._node1._prev = node2_old_next
    L._node1._element = node2_old_element

    L._node2._next = node1_old_next
    L._node2._prev = node1_old_next
    L._node2._element = node1_old_element

    return L
"""
L = _DoublyLinkedBase()
for i in range(10):
    L._insert_between(i, L._header,L._trailer)

node1 = L._Node()
node2 = L._Node()
L  = swapdouble(L,node1,node2)
"""
