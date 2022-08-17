from LinkedStack import LinkedStack

def reverse_linked_list(head):
    """
    given head, reverse the list. 
    """
    node = None # node untill which list has been reversed. 
    while True:
        new_head = head._next
        head._next = node
        node, head = head, new_head
        if head ==None:
            return node


if __name__ == "__main__":
    L = LinkedStack()
    for i in range(10):
        L.push(i)

    node = reverse_linked_list(L._head)

    # node = L._head
    while node is not None:
        print(node._element)
        node = node._next
    