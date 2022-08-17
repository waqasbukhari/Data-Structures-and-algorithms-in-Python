#!/usr/bin/env python3


from Progression import Progression

class SqProgression(Progression):
    def __init__(self, current=65536):
        super().__init__(current)
        
    def _advance(self):
        self._current = self._current ** 0.5


if __name__ == "__main__":    
    p = SqProgression(256)
    p.print_progression(10)
