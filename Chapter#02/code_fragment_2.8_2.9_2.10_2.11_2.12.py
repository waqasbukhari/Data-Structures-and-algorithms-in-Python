#!/usr/bin/env python3

import random
class Progression:
    def __init__(self, start=0):
        self._current = start
        
    def _advance(self):
        self._current += 1
        
    def __next__(self):
        answer = self._current
        self._advance()
        return answer
        
    def __iter__(self):
        return self
        
    def print_progression(self, steps = 10):
        progression = self
        for _ in range(steps):
            print(next(self), end=', ')
        print()
            
class ArithmeticProgression(Progression):
    def __init__(self, start=0, increment = 1):
        super().__init__(start)
        self._increment = increment
        
    def _advance(self):
        self._current += self._increment
        
class GeometricProgression(Progression):
    def __init__(self, start=1, base = 2):
        super().__init__(start)
        self._base = base
        
    def _advance(self):
        self._current *= self._base
        
class FibbonacciProgression(Progression):
    def __init__(self, first=0, second = 1):
        super().__init__(first)
        self._prev = second - first
        
    def _advance(self):
        self._current, self._prev = self._current + self._prev, self._current
        
    
if __name__ == '__main__':
    p = Progression(5)
    p.print_progression(15)
    ap = ArithmeticProgression(5, 2)
    ap.print_progression(15)
    gp = GeometricProgression(5, 2)
    gp.print_progression(15)
    fp = FibbonacciProgression(0, 1)
    fp.print_progression(10)
