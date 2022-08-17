from LinkedStack import LinkedStack

def reverse_linked_list(node, head):
    """
    node is tail of the list until which list has been reversed. 
    head is head of the list that has yet to be reversed. 
    """
    if head._next is None:
        head._next = node
        return head # return the new head. 

    new_head = head._next
    head._next = node # reversing 
    return reverse_linked_list(head, new_head)


if __name__ == "__main__":
    L = LinkedStack()
    for i in range(10):
        L.push(i)

    node = reverse_linked_list(None, L._head)

    # node = L._head
    while node is not None:
        print(node._element)
        node = node._next
    