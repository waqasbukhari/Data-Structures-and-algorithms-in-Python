"""
Let the lists be L1 and L2. 
i) get tail of L1 which is a sentinal. call it tail_L1.
ii) move to the real tail, tail_L1 = tail_L1._prev. 
iii) get head of L2 which is a sentinal. call it head_L2.
iv) move to the real head, head_L2 = head_L2._next. 
v) To concatenate simply tail_L1._next = head_L2, 
and L1 now is a new list, resulted from concatenating L1 and L2. 
"""