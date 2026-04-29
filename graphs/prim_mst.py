# Algorithm: Prim's MST using Min-Heap
# Time Complexity:  O((V + E) log V)
# Space Complexity: O(V + E)

import heapq


def prim_mst(num_nodes: int, graph: dict) -> tuple[int, list[tuple]]:
    """
    Find Minimum Spanning Tree using Prim's algorithm.
    graph = { node: [(neighbour, weight), ...] }

    Algorithm:
    1. Start from any node (0)
    2. Use min-heap to always pick the cheapest edge
       connecting visited to unvisited nodes
    3. Add edge and node to MST, enqueue new edges
    4. Repeat until all nodes visited

    Difference from Kruskal:
    - Kruskal: sort all edges, add greedily avoiding cycles (edge-centric)
    - Prim:    grow from one node, always pick cheapest crossing edge (node-centric)

    Applications: same as Kruskal — network, cable, road design.
    """
    visited      = set()
    mst_edges    = []
    total_weight = 0
    heap         = [(0, 0, -1)]   # (weight, node, parent)

    while heap and len(visited) < num_nodes:
        weight, node, parent = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)
        if parent != -1:
            mst_edges.append((weight, parent, node))
            total_weight += weight

        for neighbour, edge_weight in graph.get(node, []):
            if neighbour not in visited:
                heapq.heappush(heap, (edge_weight, neighbour, node))

    if len(visited) < num_nodes:
        return -1, []   # graph not connected

    return total_weight, mst_edges


if __name__ == "__main__":
    graph = {
        0: [(1,10),(2,6),(3,5)],
        1: [(0,10),(2,9),(3,15)],
        2: [(0,6),(1,9),(3,4)],
        3: [(0,5),(1,15),(2,4)],
    }

    weight, mst = prim_mst(4, graph)
    print(f"MST weight: {weight}")  # 19
    for e in mst:
        print(f"  {e[1]} -- {e[2]}  weight {e[0]}")

    # Verify Kruskal and Prim produce same total weight
    from kruskal_mst import kruskal_mst
    edges = [(10,0,1),(6,0,2),(5,0,3),(15,1,3),(4,2,3),(9,1,2)]
    kw, _ = kruskal_mst(4, edges)
    print(f"Kruskal: {kw}, Prim: {weight}, Match: {kw == weight}")  # True
