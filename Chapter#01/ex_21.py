#!/usr/bin/env python3
import sys
    
f = sys.stdin.read()#('write some lines')
lines = f.split('\n')
##
##
##lines = []
##for line in f:
##    try:
##        lines.append(line)
##    except EOFError:
##        print('End of file reached')
##
print(lines)
while lines:
    last_line = lines.pop()
    print(last_line)
    
##    
