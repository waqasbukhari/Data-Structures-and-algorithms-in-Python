#!/usr/bin/env python3

"""
method __contains__() is added to the Range class. 
The changes are enclosed within comments specifying it to be part of C-2.27.
"""

from Progression import Progression

class AbsProgression(Progression):
    def __init__(self, first=2, second=200):
        super().__init__(first)
        self._prev = second + first
        
    def _advance(self):
        self._current, self._prev = abs(self._current - self._prev), self._current


if __name__ == "__main__":    
    p = AbsProgression(2,200)
    p.print_progression(10)
