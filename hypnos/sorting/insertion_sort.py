from .base import BaseSorting


class InsertionSort(BaseSorting):
    def _sort(self):
        seq = self._sequence
        for i in range(1, len(seq)):
            for j in reversed(range(i)):
                if seq[j + 1] >= seq[j]:
                    break
                seq[j + 1], seq[j] = seq[j], seq[j + 1]
