class BaseSorting:
    def __init__(self, iterable, reverse=False):
        self._sequence = iterable
        self._sort()
    
    def _sort(self):
        raise NotImplementedError
