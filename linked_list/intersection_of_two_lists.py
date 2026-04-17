# Algorithm: Two Pointers with Length Equalisation
# Time Complexity:  O(n + m) — traverse both lists
# Space Complexity: O(1)     — no extra data structures

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


def get_intersection_node(headA, headB):
    """
    Find the node where two singly linked lists intersect.
    Returns None if they do not intersect.

    Key insight: if pointer A reaches end, redirect to headB,
    and vice versa. Both pointers travel the same total distance
    and will meet at the intersection node (or None).
    """
    if not headA or not headB:
        return None

    a, b = headA, headB

    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a


# ── test ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Build:  A: 4 -> 1 -> 8 -> 4 -> 5
    #         B: 5 -> 6 -> 1 -> 8 -> 4 -> 5  (intersect at node with value 8)
    shared = Node(8)
    shared.next = Node(4)
    shared.next.next = Node(5)

    headA = Node(4)
    headA.next = Node(1)
    headA.next.next = shared

    headB = Node(5)
    headB.next = Node(6)
    headB.next.next = Node(1)
    headB.next.next.next = shared

    result = get_intersection_node(headA, headB)
    print(result.value if result else None)  # 8
