from __future__ import annotations


class CycleError(Exception):
    """环路错误"""


def topo_sort(nodes: list[str], edges: list[tuple[str, str]]) -> list[str]:
    """拓扑排序

    nodes: 所有节点
    edges: 有向边列表，(a, b)表示 a -> b

    返回拓扑排序结果，如果有环路就抛 CycleError

    """
    adj: dict[str, list[str]] = {node: [] for node in nodes}
    indeg: dict[str, int] = {node: 0 for node in nodes}
    for a, b in edges:
        adj[a].append(b)
        indeg[b] += 1

    pool = [node for node in nodes if indeg[node] == 0]
    result: list[str] = []
    while pool:
        node = pool.pop()
        result.append(node)
        for neighbor in adj[node]:
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                pool.append(neighbor)
    if len(result) != len(nodes):
        stuck = sorted(set(nodes) - set(result))
        raise CycleError(f"cycle detected; stuck nodes: {stuck}")

    return result
