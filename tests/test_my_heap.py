import pytest

from agent_lab.my_heap import MyMinHeap


def test_peek_empty_raises() -> None:
    heap = MyMinHeap()
    with pytest.raises(IndexError):
        heap.peek()


def test_push_then_peek() -> None:
    heap = MyMinHeap()
    heap.push(3)
    heap.push(1)
    assert heap.peek() == 1
    assert len(heap) == 2


def test_pop_returns_sorted() -> None:
    heap = MyMinHeap()
    for v in [5, 3, 8, 1, 9, 2]:
        heap.push(v)
    assert [heap.pop() for _ in range(len(heap._data))] == [1, 2, 3, 5, 8, 9]


def test_interleaved() -> None:
    heap = MyMinHeap()
    heap.push(4)
    heap.push(2)
    assert heap.pop() == 2


def test_duplicates() -> None:
    heap = MyMinHeap()
    for v in [2, 2, 1, 2]:
        heap.push(v)
    assert [heap.pop() for _ in range(4)] == [1, 2, 2, 2]


def test_pop_empty_raises() -> None:
    heap = MyMinHeap()
    with pytest.raises(IndexError):
        heap.pop()
