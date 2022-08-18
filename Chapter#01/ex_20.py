import random
a = [1,2,3,4,5]
c = []

while(len(c)!=5):
    b= random.randint(1,5)
    if b not in c:
        c.append(b)
    if b in c:
            pass
        
    
print(c)
