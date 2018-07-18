# TODO: Move logic to single class
from .. import BubbleSort, SelectionSort, InsertionSort


def test_bubble_sort():
    seq = [1]
    BubbleSort(seq)
    assert seq == [1]

    seq = [1, 1, 1]
    BubbleSort(seq)
    assert seq == [1, 1, 1]

    seq = [2, 3, 1]
    BubbleSort(seq)
    assert seq == [1, 2, 3]

    seq = list(range(50))[::-1]
    BubbleSort(seq)
    assert seq == list(range(50))


def test_selection_sort():
    seq = [1]
    SelectionSort(seq)
    assert seq == [1]

    seq = [1, 1, 1]
    SelectionSort(seq)
    assert seq == [1, 1, 1]

    seq = [2, 3, 1]
    SelectionSort(seq)
    assert seq == [1, 2, 3]

    seq = list(range(50))[::-1]
    SelectionSort(seq)
    assert seq == list(range(50))


def test_insertion_sort():
    seq = [1]
    InsertionSort(seq)
    assert seq == [1]

    seq = [1, 1, 1]
    InsertionSort(seq)
    assert seq == [1, 1, 1]

    seq = [2, 3, 1]
    InsertionSort(seq)
    assert seq == [1, 2, 3]

    seq = list(range(50))[::-1]
    InsertionSort(seq)
    assert seq == list(range(50))
