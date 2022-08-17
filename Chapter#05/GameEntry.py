class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '{} scored {} runs'.format(self._name, self._score)


if __name__ == "__main__":
    A = GameEntry('Adam Khan', 1000)
    print(A)
