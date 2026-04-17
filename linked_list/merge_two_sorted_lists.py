# Algorithm: Iterative Two-Pointer Merge
# Time Complexity:  O(n + m) — n and m are lengths of the two lists
# Space Complexity: O(1)     — pointer rewiring, no new nodes

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


def merge_two_sorted_lists(l1, l2):
    """
    Merge two sorted linked lists.
    Uses a dummy head to simplify edge cases.
    Returns the head of the merged sorted list.
    """
    dummy   = Node(0)
    current = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
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
    l1 = build([1, 2, 4])
    l2 = build([1, 3, 4])
    print(to_list(merge_two_sorted_lists(l1, l2)))  # [1,1,2,3,4,4]

    print(to_list(merge_two_sorted_lists(None, build([1, 2]))))  # [1,2]
    print(to_list(merge_two_sorted_lists(None, None)))            # []
