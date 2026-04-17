# Algorithm: Iterative Pointer Reversal
# Time Complexity:  O(n) — single pass through the list
# Space Complexity: O(1) — three pointers only

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


def reverse_linked_list(head):
    """
    Reverse a singly linked list in-place.
    Returns the new head (old tail).
    """
    prev    = None
    current = head

    while current:
        next_node    = current.next
        current.next = prev
        prev         = current
        current      = next_node

    return prev


# ── helpers ──────────────────────────────────────────────────────────────────
def build(values):
    if not values:
        return None
    head = Node(values[0])
    cur  = head
    for v in values[1:]:
        cur.next = Node(v)
        cur      = cur.next
    return head

def to_list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


# ── test ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(to_list(reverse_linked_list(build([1, 2, 3, 4, 5]))))  # [5,4,3,2,1]
    print(to_list(reverse_linked_list(build([1]))))               # [1]
    print(to_list(reverse_linked_list(None)))                     # []
