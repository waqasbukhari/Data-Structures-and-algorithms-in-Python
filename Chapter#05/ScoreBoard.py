from GameEntry import GameEntry

class ScoreBoard:
    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._board = [None] * capacity

    def __getitem__(self, k):
        return self._board[k]
        
    def __str__(self):
        return '\n'.join([str(self._board[j]) for j in range(self._size)])
        
    def add(self, entry):
        if not isinstance(entry, GameEntry):
            raise ValueError('Entry should be a game entry')
            
        score = entry.get_score()
        # find index at which to place the new entry. 
        for i in range(len(self._board)):
            if self._board[i] is None:
                self._board[i] = entry
                break
                
            elif (score > self._board[i].get_score()): # index found
                for j in range(len(self._board)-1, i, -1): # move items to right to make space. 
                    self._board[j] = self._board[j-1] 
                self._board[i] = entry
                break
                
        if self._size < self._capacity:
            self._size += 1
                    
            

if __name__ == "__main__":
    S = ScoreBoard(5)
    S.add(GameEntry('Adam Khan', 1000))
    print(S)
    print()
    S.add(GameEntry('Gilchrist Tudor', 101))
    print(S)
    print()
    S.add(GameEntry('Gilchrist Tudor', 501))
    print(S)
    print()
    S.add(GameEntry('Gilchrist Tudor', 1101))
    print(S)
    print()
    S.add(GameEntry('Gilchrist Tudor', 1201))
    print(S)
    print()
    S.add(GameEntry('Gilchrist Tudor', 11010))
    print(S)
    print()
    S.add(GameEntry('Gilchrist Tudor', 1100))
    print(S)
    print()
