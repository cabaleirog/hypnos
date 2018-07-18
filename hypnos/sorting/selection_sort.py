from .base import BaseSorting


class SelectionSort(BaseSorting):
    def _sort(self):
        seq = self._sequence
        for i in range(len(seq) - 1):
            min_idx, min_val = i, seq[i]
            for j in range(i, len(seq)):
                if seq[j] < min_val:
                    min_idx, min_val = j, seq[j]
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
        