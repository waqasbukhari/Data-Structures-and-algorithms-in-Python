from Stack import ArrayStack

R = ArrayStack()
for i in range(1,4):
    R.push(i)
S = ArrayStack()
for i in range(4,6):
    S.push(i)
T = ArrayStack()
for i in range(6,10):
    T.push(i)


lenS = len(S)+len(T) #final len of S
#pushing elements of S & T onto stack R
for i in range(1,len(S)+1):
    R.push(S.pop())

for i in range(len(T)):
    R.push(T.pop())
#popping R elements 
for i in range(1,lenS+1):
    S.push(R.pop())

print(R)
print(S)
print(T)
