
# Linked List Cycle — Detecting Loops Using Fast and Slow Pointers

One of the most common problems in linked lists is detecting whether a cycle exists.

A cycle means that instead of ending at `null`, the list loops back to a previous node, creating an infinite loop.

The challenge is to detect this efficiently **without using extra space**.

---

## The Problem

Given the head of a linked list, determine if the list contains a cycle.

Return:

* `True` if a cycle exists
* `False` otherwise

Example:

```
1 → 2 → 3 → 4
     ↑     ↓
     ← ← ←
```

This list contains a cycle.

---

## Naive Approach

One approach is to store all visited nodes in a set.

If you encounter a node again, a cycle exists.

Time Complexity:

```
O(n)
```

Space Complexity:

```
O(n)
```

But we can do better.

---

## Key Idea — Fast and Slow Pointers

We use two pointers:

* `slow` moves one step at a time
* `fast` moves two steps at a time

If there is **no cycle**, the fast pointer will reach the end.

If there **is a cycle**, the fast pointer will eventually meet the slow pointer inside the loop.

---

## Why This Works

Think of it like two runners on a circular track.

The faster runner will eventually catch up to the slower one.

This guarantees detection of a cycle.

---

## Algorithm

1. Initialize two pointers at the head.
2. Move:

   * `slow` by 1 step
   * `fast` by 2 steps
3. If they meet → cycle exists
4. If `fast` reaches the end → no cycle

---

## Python Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

---

## Time Complexity

Each pointer moves through the list.

```
O(n)
```

---

## Space Complexity

No extra data structures are used.

```
O(1)
```

---

## Why This Problem Is Important

This algorithm introduces **Floyd’s Cycle Detection**, one of the most important linked list techniques.

It is widely used in problems like:

* Detecting cycles
* Finding cycle start
* Linked list intersection problems
* Repeating sequence detection

Understanding this pattern is essential for mastering linked lists.
