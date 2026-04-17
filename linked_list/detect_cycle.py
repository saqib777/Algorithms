# Algorithm: Floyd's Cycle Detection (Fast and Slow Pointers)
# Time Complexity:  O(n) — fast pointer catches slow within n steps
# Space Complexity: O(1) — two pointers only

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


def has_cycle(head) -> bool:
    """
    Detect if a singly linked list contains a cycle.
    Tortoise (slow) moves 1 step, hare (fast) moves 2 steps.
    If they meet, a cycle exists.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


# ── helper to build list with optional cycle ──────────────────────────────────
def build_with_cycle(values, cycle_pos):
    """cycle_pos = -1 means no cycle."""
    if not values:
        return None
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos != -1:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0]


# ── test ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    head = build_with_cycle([3, 2, 0, -4], cycle_pos=1)
    print(has_cycle(head))   # True

    head = build_with_cycle([1, 2], cycle_pos=-1)
    print(has_cycle(head))   # False

    print(has_cycle(None))   # False
