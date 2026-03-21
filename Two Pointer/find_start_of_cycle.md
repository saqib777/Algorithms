
# Find the Start of the Cycle in a Linked List — The Full Power of Floyd’s Algorithm

After detecting that a cycle exists in a linked list, the next natural question is:

**Where does the cycle begin?**

At first, this might seem difficult. But with a clever trick using fast and slow pointers, we can find the exact starting node of the cycle — without extra space.

---

## The Problem

Given the head of a linked list, return the node where the cycle begins.

If there is no cycle, return `None`.

Example:

```
1 → 2 → 3 → 4 → 5
         ↑     ↓
         ← ← ←
```

Output:

```
Node with value 3
```

---

## Step 1 — Detect the Cycle

We first use the **fast and slow pointer technique**:

* `slow` moves one step
* `fast` moves two steps

If they meet, a cycle exists.

---

## Step 2 — Find the Start of the Cycle

Here comes the interesting part.

Once the two pointers meet:

1. Move one pointer back to the **head**
2. Keep the other pointer at the meeting point
3. Move both pointers **one step at a time**

The point where they meet again is the **start of the cycle**

---

## Why This Works

This is based on a mathematical property of distances in the linked list.

Without going too deep into formulas, the idea is:

* The distance from head to cycle start
* Equals the distance from meeting point to cycle start

So when both pointers move at the same speed, they will meet exactly at the start of the cycle.

---

## Algorithm

1. Use fast and slow pointers to detect cycle
2. If no cycle → return None
3. Reset one pointer to head
4. Move both pointers one step at a time
5. The meeting point is the cycle start

---

## Python Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle_start(head):

    slow = head
    fast = head

    # Step 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    # Step 2: Find cycle start
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
```

---

## Time Complexity

We traverse the list at most a few times.

```
O(n)
```

---

## Space Complexity

No extra memory is used.

```
O(1)
```

---

## Why This Problem Is Important

This problem is a deeper extension of cycle detection and shows a strong understanding of linked list behavior.

It is often asked as a follow-up question in interviews.

It also strengthens your understanding of:

* Pointer movement logic
* Mathematical reasoning in algorithms
* Linked list traversal techniques

Mastering this makes many linked list problems much easier to approach.
