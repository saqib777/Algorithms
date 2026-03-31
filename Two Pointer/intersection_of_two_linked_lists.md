
# Intersection of Two Linked Lists — A Clever Pointer Switching Trick

Sometimes two linked lists merge into a common tail.

The challenge is to find the **node where both lists intersect**.

At first, it may seem like we need extra memory or length calculations. But there is a very clever way to solve this using just two pointers.

---

## The Problem

Given the heads of two singly linked lists, return the node at which they intersect.

If the two linked lists do not intersect, return `None`.

Example:

```
List A: 1 → 2 → 3 → 4 → 5
                      ↑
List B:       9 → 4 → 5
```

Output:

```
Node with value 4
```

---

## Key Idea

We use two pointers:

* `p1` starts at head of list A
* `p2` starts at head of list B

We traverse both lists.

When a pointer reaches the end of a list, we redirect it to the **head of the other list**.

---

## Why This Works

Let’s say:

* Length of A = a + c
* Length of B = b + c

Where:

* `c` is the common part (intersection)
* `a` and `b` are unique parts

By switching heads:

* `p1` travels: A → B
* `p2` travels: B → A

Both pointers will travel the same total distance:

```
a + c + b + c
```

So they will meet at the intersection point.

If no intersection exists, both pointers will eventually reach `None`.

---

## Algorithm

1. Initialize two pointers at both heads
2. Traverse lists
3. When pointer reaches end, switch to the other list
4. Continue until pointers meet
5. Return the meeting node

---

## Python Implementation

```python id="w61khy"
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_intersection_node(headA, headB):

    if not headA or not headB:
        return None

    p1 = headA
    p2 = headB

    while p1 != p2:

        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA

    return p1
```

---

## Time Complexity

Each pointer traverses both lists.

```
O(n + m)
```

---

## Space Complexity

No extra space is used.

```
O(1)
```

---

## Why This Problem Is Important

This problem introduces a **pointer switching technique**, which is different from:

* Opposite direction pointers
* Fast–slow pointers

It teaches how to equalize distances without explicitly calculating lengths.

This idea appears in several linked list problems and is highly valued in interviews.
