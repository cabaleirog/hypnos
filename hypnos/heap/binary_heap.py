class HeapUnderflowError(BaseException):
    pass


class HeapOverflowError(BaseException):
    pass


class BinaryHeap:
    def __init__(self, iterable=None, in_place=True):
        self._heap = []
        self._initialize(iterable)

    def _initialize(self, iterable):
        if iterable:
            # TODO: Improve, there is a faster approach.
            for item in iterable:
                self.push(item)

    def push(self, item):
        self._heap.append(item)
        self._sift_up(len(self._heap) - 1)

    def pop(self):
        if self.is_empty:
            raise HeapUnderflowError('Heap is empty.')
        if self.size == 1:
            return self._heap.pop()
        first_item = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._sift_down(0)
        return first_item
    
    def peek(self):
        if self.is_empty:
            raise HeapUnderflowError('Heap is empty.')
        return self._heap[0]

    def _sift_up(self, idx):
        raise NotImplementedError

    def _sift_down(self, idx):
        raise NotImplementedError

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    @property
    def size(self):
        return len(self._heap)

    @property
    def is_empty(self):
        return self.size == 0


class MinBinaryHeap(BinaryHeap):
    def _sift_up(self, idx):
        if idx == 0:
            return
        parent_idx = (idx - 1) // 2
        if self._heap[idx] < self._heap[parent_idx]:
            self._swap(idx, parent_idx)
            self._sift_up(parent_idx)

    def _sift_down(self, idx):
        # TODO: Improve implementation
        heap = self._heap
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left >= len(heap):
            return
        if right >= len(heap):
            smallest = left
        else:
            smallest = left if heap[left] < heap[right] else right
        if heap[idx] > heap[smallest] or heap[idx] > heap[smallest]:
            self._swap(idx, smallest)
            self._sift_down(smallest)




class MaxBinaryHeap(BinaryHeap):
    pass
