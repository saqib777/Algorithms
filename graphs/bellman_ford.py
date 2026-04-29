# Algorithm: Bellman-Ford
# Time Complexity:  O(V * E) — relax all edges V-1 times
# Space Complexity: O(V)

def bellman_ford(num_nodes: int, edges: list[tuple], start: int) -> dict:
    """
    Find shortest paths from start to all nodes.
    Handles negative weight edges (unlike Dijkstra).
    Detects negative weight cycles.

    edges = list of (u, v, weight)

    Algorithm:
    1. Initialize distances to infinity, start = 0
    2. Relax all edges V-1 times
       (longest shortest path has at most V-1 edges)
    3. Run one more pass — if any distance still decreases,
       a negative weight cycle exists

    Applications: currency arbitrage detection, network routing (RIP protocol).
    """
    dist = {i: float('inf') for i in range(num_nodes)}
    dist[start] = 0

    for _ in range(num_nodes - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v]  = dist[u] + w
                updated  = True
        if not updated:
            break   # early termination if no updates

    # Detect negative cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return {'error': 'Negative weight cycle detected'}

    return dist


def bellman_ford_with_path(num_nodes: int, edges: list[tuple],
                            start: int, end: int) -> tuple:
    """
    Variant: return (distance, path) from start to end.
    Tracks predecessor array for path reconstruction.
    """
    dist = {i: float('inf') for i in range(num_nodes)}
    prev = {i: None         for i in range(num_nodes)}
    dist[start] = 0

    for _ in range(num_nodes - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return float('inf'), []

    path, curr = [], end
    while curr is not None:
        path.append(curr)
        curr = prev[curr]

    return dist[end], path[::-1]


if __name__ == "__main__":
    edges = [(0,1,4),(0,2,5),(1,3,3),(2,1,-6),(3,2,2)]
    print(bellman_ford(4, edges, 0))
    # {0:0, 1:-1, 2:4, 3:2} or negative cycle

    simple = [(0,1,1),(0,2,4),(1,2,2),(1,3,5),(2,3,1)]
    print(bellman_ford(4, simple, 0))   # {0:0,1:1,2:3,3:4}

    dist, path = bellman_ford_with_path(4, simple, 0, 3)
    print(dist, path)   # 4  [0,1,2,3]
