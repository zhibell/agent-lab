import pytest

from agent_lab.my_topo import CycleError, topo_sort


def is_valid_order(nodes: list[str], edges: list[tuple[str, str]], order: list[str]) -> bool:
    """性质检查：order 是否为合法拓扑序。"""
    if sorted(order) != sorted(nodes):
        return False
    pos = {node: i for i, node in enumerate(order)}
    return all(pos[u] < pos[v] for u, v in edges)


def test_simple_chain() -> None:
    assert topo_sort(["A", "B", "C"], [("A", "B"), ("B", "C")]) == ["A", "B", "C"]


def test_order_is_valid_not_unique() -> None:
    nodes = ["P", "Q", "R", "S", "T"]
    edges = [("P", "R"), ("Q", "R"), ("Q", "S"), ("R", "T"), ("S", "T")]
    order = topo_sort(nodes, edges)
    assert is_valid_order(nodes, edges, order)  # 只验性质，不验具体序列


def test_independent_nodes() -> None:
    order = topo_sort(["X", "Y"], [])
    assert is_valid_order(["X", "Y"], [], order)


def test_cycle_raises() -> None:
    with pytest.raises(CycleError):
        topo_sort(["A", "B"], [("A", "B"), ("B", "A")])


def test_downstream_of_cycle_also_stuck() -> None:  # C 不在环里，也必须报错
    with pytest.raises(CycleError):
        topo_sort(["A", "B", "C"], [("A", "B"), ("B", "A"), ("B", "C")])


def test_empty_graph() -> None:
    assert topo_sort([], []) == []
