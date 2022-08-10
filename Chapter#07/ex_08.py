from LinkedDeque import LinkedDeque

def find_middle(D):
    head = D._header
    tail = D._trailer
    while True:
        # In case of array with even numnber of elements
        if head._next is tail and tail._prev is head:
            return 'Middle elements is ,{}'.format(tail._element)
        # In case of array with odd numnber of elements
        if head._next is tail._prev:
            return 'Middle elements is {}'.format(head._next._element)
        head, tail = head._next, tail._prev
        
        
    
    
    
        
if __name__ == '__main__':
    D = LinkedDeque()

    for i in range(11):
        D.insert_first(i)

    print(find_middle(D))
