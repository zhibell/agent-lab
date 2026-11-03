from __future__ import annotations


class MyMinHeap:
    """最小堆，peek O(1);push/pop O(log n)"""

    def __init__(self) -> None:
        self._data: list[int] = []

    def __len__(self) -> int:
        return len(self._data)

    def _swap(self, i: int, j: int) -> None:
        """交换数组中两数"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_up(self, i: int) -> None:
        """把位置i的元素与父比较，比父节点小就交换并且继续上浮；到根或不再更小则停止"""
        parent = (i - 1) // 2
        if i > 0 and self._data[i] < self._data[parent]:
            self._swap(i, parent)
            self._sift_up(parent)

    def _sift_down(self, i: int) -> None:
        """与较小的孩子比较，孩子更小就交换下潜；无孩子或者不再有更小的孩子就停止"""
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self._data) and self._data[left] < self._data[smallest]:
            smallest = left
        if right < len(self._data) and self._data[right] < self._data[smallest]:
            smallest = right
        if smallest != i:
            self._swap(i, smallest)
            self._sift_down(smallest)

    def peek(self) -> int:
        """返回最小值但不删除；空堆抛出 IndexError。O(1)"""
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def push(self, value: int) -> None:
        """追加到数组末尾，再对新元素上浮。O(log n)"""
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> int:
        """取出最小值： 根与末尾交换 -> 弹出末尾 -> 新根下潜。空堆抛 IndexError。O(log n)"""
        if not self._data:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self._data) - 1)
        min_value = self._data.pop()
        self._sift_down(0)
        return min_value
