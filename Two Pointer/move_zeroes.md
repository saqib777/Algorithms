
# Move Zeroes — Rearranging an Array Using Two Pointers

In many array problems, the challenge is not just to find values but to **rearrange elements efficiently without using extra space**.

A classic example of this idea is the **Move Zeroes** problem.

The goal is simple: move all zero values to the end of the array while keeping the relative order of the other elements unchanged.

---

## The Problem

You are given an integer array `nums`.

Move all `0`s to the end of the array while maintaining the **relative order of the non-zero elements**.

You must do this **in-place** without making a copy of the array.

Example:

```id="n2re4h"
nums = [0,1,0,3,12]
```

Output:

```id="yzwc9j"
[1,3,12,0,0]
```

---

## Brute Force Idea

One simple approach would be:

1. Create a new list of all non-zero elements.
2. Count the number of zeroes.
3. Append that many zeroes at the end.

But this requires **extra memory**, which the problem asks us to avoid.

---

## Key Idea

We use **two pointers**.

* `fast` pointer scans the array.
* `slow` pointer tracks where the next non-zero element should go.

When a non-zero value is found, we place it at the `slow` position and move the slow pointer forward.

---

## Example Walkthrough

Array:

```id="n9o8ui"
[0,1,0,3,12]
```

Pointer movement:

```
fast scans → finds non-zero
slow marks next valid position
```

Result evolves like:

```
[1,3,12,0,0]
```

---

## Algorithm

1. Initialize `slow = 0`.
2. Traverse the array using `fast`.
3. If `nums[fast]` is not zero:

   * Swap `nums[slow]` and `nums[fast]`
   * Increment `slow`.
4. Continue until the end of the array.

---

## Python Implementation

```python
def move_zeroes(nums):

    slow = 0

    for fast in range(len(nums)):

        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    return nums


# Example
nums = [0,1,0,3,12]

print(move_zeroes(nums))
```

Output:

```
[1, 3, 12, 0, 0]
```

---

## Time Complexity

We scan the array once.

```
O(n)
```

---

## Space Complexity

The operation is done in-place.

```
O(1)
```

---

## Why This Problem Matters

Move Zeroes strengthens the idea of **in-place array transformations using two pointers**.

This pattern appears frequently in real algorithm problems, including:

* Partitioning arrays
* Removing elements
* Stable rearrangement problems

Mastering this technique makes many array manipulation tasks much easier.
