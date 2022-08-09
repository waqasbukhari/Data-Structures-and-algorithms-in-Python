# implement a double-ended queue. 
class Dequeue:
    def __init__(self):
        self._A = [None] * 10
        self._capacity = 10 # initial capacity. 
        self._size = 0 # array size. 
        self._first = 0 # element where first eleemnt is added. 
        
    def __len__(self):
        return self._size
    
    def add_last(self, e):
        if 1>e:
            return
        if self._size == self._capacity: 
            self._resize(2*self._capacity)
            
        idx = (self._first + self._size) % self._capacity
        self._A[idx] = e
        self._size += 1
        
    def add_first(self, e):
        if 1>e:
            return
        if self._size == self._capacity: 
            self._resize(2*self._capacity)
            
        self._first = (self._first -1) % self._capacity
        self._A[self._first] = e
        self._size += 1
        
    def delete_last(self):
        if len(self) == 0:
            return 
        idx = (self._first + self._size -1) % self._capacity
        answer = self._A[idx]
        self._A[idx] = None
        self._size -= 1
        return answer


    def delete_first(self):
        if len(self) == 0:
            return 
        idx = (self._first) % self._capacity
        answer = self._A[idx]
        self._A[idx] = None
        self._size -= 1
        self._first =   (self._first + 1) % self._capacity

        return answer

            
    def _resize(self, capacity):
        B = [None] * capacity
        for i in range(self._size):
            B[i] = self._A[(self._first + i) % self._capacity]
            
        self._A = B
        self._capacity = capacity
        self._first = 0
            

class FrontMiddleBackQueue:

    def __init__(self):
        self._front = Dequeue()
        self._back = Dequeue()
        self._middle = None

    def __len__(self):
        return len(self._front) + len(self._back) + int(self._middle!=None)


    def pushFront(self, val: int) -> None:
        self._front.add_first(val)
        self._adjust_arrays()
            
        
    def pushMiddle(self, val: int) -> None:
        answer = self._middle
        self._middle = val
        if answer != None:
            if len(self._back) == len(self._front):
                self._back.add_first(answer) 
            else:
                self._front.add_last(answer)
            self._adjust_arrays()
        
    def pushBack(self, val: int) -> None:
        self._back.add_last(val)
        self._adjust_arrays()


    def _adjust_arrays(self):
        if len(self) == 0:
            return

        if self._middle == None: # populate it. 
            if len(self._front) >= len(self._back):
                self._middle = self._front.delete_last()
            else:
                self._middle = self._back.delete_first()
        else:
            if len(self._front) > len(self._back):
                self._back.add_first(self._middle)
                self._middle = self._front.delete_last()
            elif (len(self._back) - len(self._front) > 1):
                self._front.add_last(self._middle)
                self._middle = self._back.delete_first()

    def popFront(self) -> int:
        if len(self) == 0:
            answer = -1
        else:
            if len(self._front) == 0:
                # if len(self) is not 0, self._middle would exist.
                # so, if len(self._front) is zero, then pop self._middle. 
                answer = self.popMiddle()
            else:
                answer = self._front.delete_first()

        self._adjust_arrays()

        return answer
        

    def popMiddle(self) -> int:
        if len(self) ==0:
            return -1

        answer = self._middle
        self._middle = None
        
        self._adjust_arrays()

        return answer

    def popBack(self) -> int:
        if len(self) == 0:
            answer = -1
        else:
            if len(self._back) == 0:
                # if len(self) is not 0, self._middle would exist.
                # so, if len(self._front) is zero, then pop self._middle. 
                answer = self.popMiddle()
            else:
                answer = self._back.delete_last()

        self._adjust_arrays()
        return answer

if __name__ == "__main__":
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    q.pushFront(2)
    q.pushFront(3)
    q.pushFront(4)
    print(q._front._A)
    print(q._middle)
    print(q._back._A)
    print(q.popBack())
    print(q.popBack())
    print(q.popBack())
    print(q.popBack())
    print(q.popFront())