# Algorithm: Kruskal's MST using Union-Find
# Time Complexity:  O(E log E) — dominated by sorting edges
# Space Complexity: O(V + E)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank   = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


def kruskal_mst(num_nodes: int, edges: list[tuple]) -> tuple[int, list[tuple]]:
    """
    Find Minimum Spanning Tree using Kruskal's algorithm.
    edges = list of (weight, u, v)

    Algorithm:
    1. Sort edges by weight ascending
    2. For each edge, add it to MST if it connects two different components
       (use Union-Find to check and merge)
    3. Stop when V-1 edges added (MST is complete)

    A Minimum Spanning Tree connects all nodes with minimum total edge weight
    and no cycles.

    Applications: network design, clustering, image segmentation.
    """
    edges_sorted = sorted(edges, key=lambda x: x[0])
    uf           = UnionFind(num_nodes)
    mst_edges    = []
    total_weight = 0

    for weight, u, v in edges_sorted:
        if uf.union(u, v):
            mst_edges.append((weight, u, v))
            total_weight += weight
            if len(mst_edges) == num_nodes - 1:
                break   # MST complete

    if len(mst_edges) < num_nodes - 1:
        return -1, []   # graph is not connected

    return total_weight, mst_edges


if __name__ == "__main__":
    edges = [
        (10, 0, 1),(6, 0, 2),(5, 0, 3),
        (15, 1, 3),(4, 2, 3),(9, 1, 2),
    ]
    weight, mst = kruskal_mst(4, edges)
    print(f"MST weight: {weight}")   # 19
    for e in mst:
        print(f"  {e[1]} -- {e[2]}  weight {e[0]}")
