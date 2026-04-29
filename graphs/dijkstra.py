# Algorithm: Dijkstra's Shortest Path (Min-Heap)
# Time Complexity:  O((V + E) log V) — heap operations
# Space Complexity: O(V + E)         — graph + distance array

import heapq


def dijkstra(graph: dict, start: int) -> dict[int, float]:
    """
    Find shortest path from start to all other nodes.
    graph = { node: [(neighbour, weight), ...] }
    Returns dict of { node: shortest_distance }.

    Only works with non-negative edge weights.
    For negative weights use Bellman-Ford.

    Algorithm:
    1. Initialize distances to infinity, start to 0
    2. Use min-heap to always process nearest unvisited node
    3. For each node, relax all outgoing edges
    4. Skip if we have already found a shorter path (lazy deletion)
    """
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]   # (distance, node)

    while heap:
        curr_dist, node = heapq.heappop(heap)

        if curr_dist > dist[node]:
            continue    # stale entry — skip

        for neighbour, weight in graph.get(node, []):
            new_dist = curr_dist + weight
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                heapq.heappush(heap, (new_dist, neighbour))

    return dist


def dijkstra_with_path(graph: dict, start: int, end: int) -> tuple[float, list[int]]:
    """
    Variant: return (shortest_distance, actual_path) from start to end.
    Tracks predecessors to reconstruct the path.
    """
    dist    = {node: float('inf') for node in graph}
    prev    = {node: None         for node in graph}
    dist[start] = 0
    heap    = [(0, start)]

    while heap:
        curr_dist, node = heapq.heappop(heap)
        if curr_dist > dist[node]:
            continue
        if node == end:
            break
        for neighbour, weight in graph.get(node, []):
            new_dist = curr_dist + weight
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                prev[neighbour] = node
                heapq.heappush(heap, (new_dist, neighbour))

    # Reconstruct path
    path, curr = [], end
    while curr is not None:
        path.append(curr)
        curr = prev[curr]

    return dist[end], path[::-1]


if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [],
    }

    distances = dijkstra(graph, 0)
    print(distances)   # {0:0, 1:3, 2:1, 3:4}

    dist, path = dijkstra_with_path(graph, 0, 3)
    print(dist, path)  # 4  [0, 2, 1, 3]
