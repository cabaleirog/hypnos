from .. import MinBinaryHeap, MaxBinaryHeap


def test_min_heap_heapify():
    seq = [3, 1, 5, 2, 4]
    heap = MinBinaryHeap(seq)
    assert heap.is_empty is False
    assert heap.size == 5
    assert heap.peek() == 1


def test_min_heap_pop():
    seq = [3, 1, 5, 2, 4]
    heap = MinBinaryHeap(seq)
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3
    assert heap.pop() == 4
    assert heap.pop() == 5


def test_min_heap_peek():
    seq = [3, 1, 5, 2, 4]
    heap = MinBinaryHeap(seq)
    assert heap.peek() == 1


def test_min_heap_push():
    heap = MinBinaryHeap()
    assert heap.is_empty is True
    heap.push(50)
    assert heap.is_empty is False
    assert heap.size == 1
    assert heap.peek() == 50
    heap.push(20)
    assert heap.size == 2
    assert heap.peek() == 20
    heap.push(30)
    assert heap.size == 3
    assert heap.peek() == 20
    assert heap.pop() == 20
    assert heap.size == 2
    assert heap.peek() == 30
