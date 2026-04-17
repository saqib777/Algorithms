# Algorithm: Two Pointers (Fast and Slow with N gap)
# Time Complexity:  O(n) — single pass
# Space Complexity: O(1) — two pointers only

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


def remove_nth_from_end(head, n: int):
    """
    Remove the nth node from the end of the list.
    Returns the head of the modified list.

    Approach:
    - Move fast pointer n steps ahead
    - Move both pointers until fast reaches the last node
    - slow.next is now the node to remove
    """
    dummy      = Node(0)
    dummy.next = head
    fast       = dummy
    slow       = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next


# ── helpers ───────────────────────────────────────────────────────────────────
def build(values):
    if not values: return None
    head = Node(values[0]); cur = head
    for v in values[1:]: cur.next = Node(v); cur = cur.next
    return head

def to_list(head):
    r = []
    while head: r.append(head.value); head = head.next
    return r


# ── test ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(to_list(remove_nth_from_end(build([1,2,3,4,5]), 2)))  # [1,2,3,5]
    print(to_list(remove_nth_from_end(build([1]), 1)))           # []
    print(to_list(remove_nth_from_end(build([1,2]), 1)))         # [1]
