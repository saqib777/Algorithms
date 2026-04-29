
# Algorithm: Union-Find (Disjoint Set Union) + DFS
# Time Complexity:  O(V + E) DFS | O(E * alpha(V)) Union-Find
# Space Complexity: O(V)

def has_cycle_dfs(graph: dict) -> bool:
    """
    Detect cycle in an undirected graph using DFS.
    Track parent to avoid false positives from the edge we came from.
    """
    visited = set()

    def dfs(node, parent) -> bool:
        visited.add(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                if dfs(neighbour, node):
                    return True
            elif neighbour != parent:
                return True    # back edge to non-parent = cycle
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


class UnionFind:
    """Disjoint Set Union with path compression and union by rank."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank   = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union x and y. Returns False if already in same set (cycle detected).
        """
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


def has_cycle_union_find(num_nodes: int, edges: list[tuple]) -> bool:
    """
    Detect cycle using Union-Find.
    For each edge, if both endpoints already share a root → cycle.
    """
    uf = UnionFind(num_nodes)
    for u, v in edges:
        if not uf.union(u, v):
            return True
    return False


if __name__ == "__main__":
    cyclic    = {0:[1,3], 1:[0,2], 2:[1,3], 3:[2,0]}
    acyclic   = {0:[1,2], 1:[0,3], 2:[0], 3:[1]}

    print(has_cycle_dfs(cyclic))    # True
    print(has_cycle_dfs(acyclic))   # False

    print(has_cycle_union_find(4, [(0,1),(1,2),(2,3),(3,0)]))  # True
    print(has_cycle_union_find(4, [(0,1),(1,2),(2,3)]))        # False
