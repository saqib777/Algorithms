# Algorithm: Kahn's Algorithm (BFS) + DFS Post-order
# Time Complexity:  O(V + E)
# Space Complexity: O(V + E)

from collections import deque


def topological_sort_kahn(graph: dict, num_nodes: int) -> list[int]:
    """
    Topological sort using Kahn's Algorithm (BFS + in-degree).

    A topological ordering exists only if the graph is a DAG
    (Directed Acyclic Graph). If a cycle exists, returns [].

    Algorithm:
    1. Compute in-degree for every node
    2. Add all nodes with in-degree 0 to queue
    3. Process queue: add node to result, decrement neighbours' in-degree
    4. If neighbour's in-degree becomes 0, add to queue
    5. If result length < num_nodes, a cycle exists

    Applications: build systems, task scheduling, course prerequisites.
    """
    in_degree = {i: 0 for i in range(num_nodes)}
    for node in graph:
        for neighbour in graph[node]:
            in_degree[neighbour] += 1

    queue  = deque([n for n in range(num_nodes) if in_degree[n] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbour in graph.get(node, []):
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    return result if len(result) == num_nodes else []


def topological_sort_dfs(graph: dict, num_nodes: int) -> list[int]:
    """
    Topological sort using DFS post-order.
    Nodes are appended after all their dependencies are processed.
    Reverse the result to get topological order.
    Returns [] if cycle detected.
    """
    visited = [0] * num_nodes   # 0=unvisited 1=visiting 2=done
    result  = []
    has_cycle = [False]

    def dfs(node):
        if has_cycle[0]:
            return
        if visited[node] == 1:
            has_cycle[0] = True
            return
        if visited[node] == 2:
            return
        visited[node] = 1
        for neighbour in graph.get(node, []):
            dfs(neighbour)
        visited[node] = 2
        result.append(node)

    for node in range(num_nodes):
        if visited[node] == 0:
            dfs(node)

    return [] if has_cycle[0] else result[::-1]


if __name__ == "__main__":
    # Graph: 5→2, 5→0, 4→0, 4→1, 2→3, 3→1
    graph = {5:[2,0], 4:[0,1], 2:[3], 3:[1], 0:[], 1:[]}

    print(topological_sort_kahn(graph, 6))  # [4,5,0,2,3,1] or valid order
    print(topological_sort_dfs(graph, 6))   # [5,4,2,3,1,0] or valid order

    # Cyclic graph — should return []
    cyclic = {0:[1], 1:[2], 2:[0]}
    print(topological_sort_kahn(cyclic, 3)) # []
    print(topological_sort_dfs(cyclic, 3))  # []
