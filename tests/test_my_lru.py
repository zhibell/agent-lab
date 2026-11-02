from agent_lab.my_lru import MyLRU


def test_get_missing() -> None:
    lru = MyLRU(2)
    assert lru.get("a") is None


def test_put_and_get() -> None:
    lru = MyLRU(2)
    lru.put("a", 1)
    assert lru.get("a") == 1


def test_lru_evicts_oldest() -> None:
    lru = MyLRU(2)
    lru.put("a", 1)
    lru.put("b", 2)
    lru.put("c", 3)
    assert lru.get("a") is None
    assert lru.get("b") == 2
    assert lru.get("c") == 3


def test_get_refreshes_recency() -> None:
    lru = MyLRU(2)
    lru.put("a", 1)
    lru.put("b", 2)
    assert lru.get("a") == 1
    lru.put("c", 3)
    assert lru.get("b") is None
    assert lru.get("a") == 1


def test_update_existing_key() -> None:
    lru = MyLRU(2)
    lru.put("a", 1)
    lru.put("a", 99)
    assert lru.get("a") == 99
