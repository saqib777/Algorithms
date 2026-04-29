# Algorithm: Floyd-Warshall (All-Pairs Shortest Path)
# Time Complexity:  O(V^3)
# Space Complexity: O(V^2)

def floyd_warshall(graph: list[list[float]]) -> list[list[float]]:
    """
    Find shortest paths between ALL pairs of nodes.
    graph[i][j] = weight of edge i→j (float('inf') if no edge, 0 if i==j).

    Unlike Dijkstra (single source) or Bellman-Ford (single source),
    Floyd-Warshall gives every node to every other node.

    Works with negative weights. Detects negative cycles
    (diagonal becomes negative).

    Core recurrence:
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for each intermediate node k.
    """
    n    = len(graph)
    dist = [row[:] for row in graph]   # deep copy

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Check for negative cycles (any diagonal < 0)
    for i in range(n):
        if dist[i][i] < 0:
            raise ValueError(f"Negative cycle detected involving node {i}")

    return dist


def floyd_warshall_with_paths(graph: list[list[float]]):
    """
    Variant: also reconstruct the actual shortest paths.
    next_node[i][j] = next node on the shortest path from i to j.
    """
    n         = len(graph)
    dist      = [row[:] for row in graph]
    next_node = [[j if graph[i][j] != float('inf') else None
                  for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j]      = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    def get_path(u: int, v: int) -> list[int]:
        if next_node[u][v] is None:
            return []
        path = [u]
        while u != v:
            u = next_node[u][v]
            path.append(u)
        return path

    return dist, get_path


if __name__ == "__main__":
    INF = float('inf')
    graph = [
        [0,   3,   INF, 7  ],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1  ],
        [2,   INF, INF, 0  ],
    ]

    dist = floyd_warshall(graph)
    for row in dist:
        print([x if x != INF else '∞' for x in row])

    dist2, get_path = floyd_warshall_with_paths(graph)
    print(get_path(0, 2))   # [0, 1, 2]
    print(get_path(3, 1))   # [3, 0, 1]
