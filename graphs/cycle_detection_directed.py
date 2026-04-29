# Algorithm: DFS with 3-colour marking
# Time Complexity:  O(V + E)
# Space Complexity: O(V)

def has_cycle_directed(graph: dict) -> bool:
    """
    Detect cycle in a directed graph using DFS 3-colour marking.

    States:
        0 = WHITE — unvisited
        1 = GREY  — currently in DFS call stack
        2 = BLACK — fully processed

    A back edge to a GREY node indicates a cycle.
    Unlike undirected graphs, we cannot use parent tracking —
    we need the full call stack state.
    """
    color = {node: 0 for node in graph}

    def dfs(node) -> bool:
        color[node] = 1   # GREY — mark as in progress

        for neighbour in graph.get(node, []):
            if color.get(neighbour, 0) == 1:
                return True   # back edge to GREY node = cycle
            if color.get(neighbour, 0) == 0:
                if dfs(neighbour):
                    return True

        color[node] = 2   # BLACK — fully processed
        return False

    for node in graph:
        if color[node] == 0:
            if dfs(node):
                return True

    return False


def find_all_cycles(graph: dict) -> list[list]:
    """
    Find and return all cycles in a directed graph.
    Uses Johnson's algorithm concept — DFS with tracking.
    Returns list of cycles, each as a list of nodes.
    """
    all_cycles = []
    path       = []
    path_set   = set()
    visited    = set()

    def dfs(start, node):
        path.append(node)
        path_set.add(node)

        for neighbour in graph.get(node, []):
            if neighbour == start and len(path) > 1:
                all_cycles.append(list(path))
            elif neighbour not in path_set and neighbour not in visited:
                dfs(start, neighbour)

        path.pop()
        path_set.discard(node)

    nodes = list(graph.keys())
    for node in nodes:
        dfs(node, node)
        visited.add(node)

    return all_cycles


if __name__ == "__main__":
    cyclic  = {0:[1], 1:[2], 2:[3], 3:[1]}
    acyclic = {0:[1,2], 1:[3], 2:[3], 3:[]}

    print(has_cycle_directed(cyclic))   # True
    print(has_cycle_directed(acyclic))  # False

    self_loop = {0:[0], 1:[2], 2:[]}
    print(has_cycle_directed(self_loop)) # True

    cycles = find_all_cycles({0:[1], 1:[2], 2:[0,3], 3:[4], 4:[3]})
    for c in cycles:
        print(c)
