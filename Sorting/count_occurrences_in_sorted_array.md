# Count Occurrences in Sorted Array

## Problem Statement

Given a **sorted array** `nums` and a target value `target`, return the **number of times** the target appears in the array.

If the target does not exist, return `0`.

You must write an algorithm with **O(log n)** time complexity.

---

## Example

Input:

```python
nums = [5, 7, 7, 8, 8, 8, 10]
target = 8
```

Output:

```python
3
```

---

Input:

```python
nums = [1, 2, 3, 4]
target = 5
```

Output:

```python
0
```

---

## Intuition

Because the array is sorted, all occurrences of the target will appear **contiguously**.

So the idea is:

1. Find the **first occurrence**
2. Find the **last occurrence**
3. Compute count:

```python
count = last_index - first_index + 1
```

If target is not found, return 0.

This is directly based on:

Boundary Binary Search.

---

## Approach

We reuse the logic from:

First and Last Occurrence problem.

Steps:

1. Find first index
2. If first index == -1 → return 0
3. Find last index
4. Return last − first + 1

---

## Algorithm

### First Occurrence

Move left after finding target.

### Last Occurrence

Move right after finding target.

---

## Dry Run

Array:

```python
[5, 7, 7, 8, 8, 8, 10]
target = 8
```

First occurrence → index 3
Last occurrence → index 5

Count:

```python
5 - 3 + 1 = 3
```

---

## Python Implementation

```python
def find_first(nums, target):
    low = 0
    high = len(nums) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            first = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first


def find_last(nums, target):
    low = 0
    high = len(nums) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last


def count_occurrences(nums, target):
    first = find_first(nums, target)

    if first == -1:
        return 0

    last = find_last(nums, target)

    return last - first + 1


# Example usage
nums = [5, 7, 7, 8, 8, 8, 10]
target = 8

print(count_occurrences(nums, target))  # Output: 3
```

---

## Time Complexity

Two binary searches:

```
O(log n)
```

---

## Space Complexity

```
O(1)
```

No extra memory used.

---

## Key Learning

Important identity:

```
Count = Last Index − First Index + 1
```

This works only because the array is sorted.

This problem reinforces:

* Boundary Binary Search
* Lower Bound / Upper Bound concept
* First and Last Occurrence logic

---

## Interview Tip

Whenever you see:

* Count duplicates
* Frequency in sorted array
* Number of occurrences

Think:

Find first + find last.

---

## Related Problems

* First and Last Occurrence of Element
* Lower Bound and Upper Bound
* Search Insert Position
* Floor and Ceil in Sorted Array
