
# Palindrome Linked List — Using Fast and Slow Pointers

Checking whether a structure reads the same forwards and backwards is a common algorithm problem. While it’s easy with strings or arrays, linked lists introduce a new challenge because they cannot be accessed by index.

To solve this efficiently, we combine two important techniques:

* **Fast and slow pointers**
* **Reversing part of a linked list**

---

## The Problem

Given the head of a singly linked list, determine whether it is a palindrome.

A palindrome means the sequence of values is the same forward and backward.

Example:

```
1 → 2 → 2 → 1
```

Output:

```
True
```

Another example:

```
1 → 2
```

Output:

```
False
```

---

## Key Idea

To check if the list is a palindrome, we need to compare the **first half** of the list with the **second half**.

Steps:

1. Find the middle of the list.
2. Reverse the second half.
3. Compare both halves.

The challenge is finding the middle efficiently.

---

## Fast and Slow Pointer Technique

We use two pointers:

```
slow → moves one step
fast → moves two steps
```

When the fast pointer reaches the end, the slow pointer will be at the **middle of the list**.

Example:

```
1 → 2 → 3 → 2 → 1
      ↑
     slow
```

---

## Algorithm

1. Use fast and slow pointers to find the middle.
2. Reverse the second half of the linked list.
3. Compare the first half with the reversed second half.
4. If all values match, it is a palindrome.

---

## Python Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    left = head
    right = prev

    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
```

---

## Time Complexity

We traverse the list a few times.

```
O(n)
```

---

## Space Complexity

The list is modified in-place.

```
O(1)
```

---

## Why This Problem Is Important

This problem introduces an important variation of the two-pointer technique called **fast and slow pointers**.

This pattern is widely used in linked list problems such as:

* Detecting cycles in linked lists
* Finding the middle of a list
* Reordering linked lists
* Splitting linked lists

Learning this technique makes many linked list problems much easier to solve.
