from __future__ import annotations

from dataclasses import dataclass


@dataclass
class _Node:
    key: object
    value: object
    prev: _Node | None = None
    next: _Node | None = None


class MyLRU:
    """容量固定的LRU缓存

    get/put：不存在的键返回 None/插入新键
    容量满时淘汰 tail.prev （最久未使用）

    """

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._capacity = capacity
        self._map: dict[object, _Node] = {}
        self._head = _Node(key=None, value=None)
        self._tail = _Node(key=None, value=None)
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node: _Node) -> None:
        """
        把node从链表摘除（不懂_map）,O(1)
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        # TODO 1: 让node.prev直接抓住node.next,双向都要接上

    def _add_front(self, node: _Node) -> None:
        """
        把node插到 head 之后（表示最近用过）,O(1)
        """
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node
        # TODO 2: 改四根指针——node 与 head、node 与原 head.next

    def get(self, key: object) -> object:
        """
        命中：摘下→插回头部→返回 value；未命中：返回 None。O(1)。
        """
        node = self._map.get(key)
        if node is None:
            return None
        self._remove(node)
        self._add_front(node)
        return node.value

        # TODO 3: _map查key；查不到返回None;查到后_remove +_add_front

    def put(self, key: object, value: object) -> None:
        """
        已存在：更新value并挪到头部；不存在：新键插头部，超容量则淘汰。 O(1)
        """
        node = self._map.get(key)
        if node is not None:
            node.value = value
            self._remove(node)
            self._add_front(node)
        else:
            node = _Node(key=key, value=value)
            self._map[key] = node
            self._add_front(node)
            if len(self._map) > self._capacity:
                victim = self._tail.prev
                self._remove(victim)
                del self._map[victim.key]
        # TODO 4: 分"已存在/新键"两路；新键后len(self._map) > self.capacity
        #         时，victim = self._tail.prev.)remove(victim) 且 del self.map[victim.key]
