from .base import BaseSorting


class BubbleSort(BaseSorting):
    def _sort(self):
        seq = self._sequence
        for i in range(len(seq) - 1):
            for j in range(len(seq) - i - 1):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]
