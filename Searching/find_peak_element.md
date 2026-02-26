# Find Peak Element

## Problem Statement

A **peak element** is an element that is strictly greater than its neighbors.

Given an integer array `nums`, find a peak element and return its index.

If the array contains multiple peaks, return the index of **any one** of them.

You must write an algorithm with **O(log n)** time complexity.

You may assume:

```python
nums[-1] = -∞
nums[n] = -∞
```

This means the boundaries can also be peaks.

---

## Example

Input:

```python
nums = [1, 2, 3, 1]
```

Output:

```python
2
```

Explanation: 3 is a peak element.

---

Input:

```python
nums = [1, 2, 1, 3, 5, 6, 4]
```

Output:

```python
5
```

Explanation: 6 is a peak element.

---

## Intuition

We use **Binary Search** because we can eliminate half of the array based on slope direction.

Key observation:

If:

```python
nums[mid] < nums[mid + 1]
```

Then a peak must exist on the **right side**.

Why?

Because the array is going upward, and eventually it must come down (since the end is −∞), so a peak must exist.

Otherwise:

```python
nums[mid] > nums[mid + 1]
```

A peak exists on the **left side (including mid)**.

So we keep narrowing the search space until only one element remains.

---

## Algorithm (Binary Search on Condition)

1. Initialize pointers:

```python
low = 0
high = len(nums) - 1
```

2. While `low < high`:

* Find middle index:

```python
mid = (low + high) // 2
```

* If right neighbor is greater:

```python
nums[mid] < nums[mid + 1]
```

Move right:

```python
low = mid + 1
```

* Else move left:

```python
high = mid
```

3. When loop ends:

```python
low == high
```

This index is the peak.

Return `low`.

---

## Dry Run

Array:

```python
[1, 2, 3, 1]
```

Step 1:

```python
low = 0, high = 3
mid = 1 → nums[1] = 2
```

Compare:

```python
nums[1] < nums[2] → 2 < 3 → True
```

Move right:

```python
low = mid + 1 = 2
```

Step 2:

```python
low = 2, high = 3
mid = 2 → nums[2] = 3
```

Compare:

```python
nums[2] > nums[3] → 3 > 1 → True
```

Move left:

```python
high = mid = 2
```

Now:

```python
low = 2, high = 2
```

Return:

```python
2
```

Peak found.

---

## Python Implementation

```python
def findPeakElement(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low


# Example usage
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 1, 3, 5, 6, 4]

print(findPeakElement(nums1))  # Output: 2
print(findPeakElement(nums2))  # Output: 5 (or another valid peak)
```

---

## Time Complexity

Binary search halves the search space every iteration.

```python
Time Complexity: O(log n)
```

---

## Space Complexity

No extra memory used.

```python
Space Complexity: O(1)
```

---

## Key Learning

Very important insight:

> We are not searching for a value.
> We are searching for a **pattern (increasing or decreasing slope)**.

This is called:

```python
Binary Search on Condition
```

This concept is heavily used in advanced problems like:

* Mountain Array problems
* Minimum in Rotated Sorted Array
* Binary Search on Answer (Optimization problems)

---

## Interview Tip

If confused, remember one rule:

> Always compare `mid` with `mid + 1`.

That alone is enough to decide the direction.

---

## Related Problems

* Search in Bitonic Array
* Find Minimum in Rotated Sorted Array
* Peak Index in Mountain Array
* Binary Search on Answer Problems
