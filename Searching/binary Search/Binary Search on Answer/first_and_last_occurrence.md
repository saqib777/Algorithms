# First and Last Occurrence of Element in Sorted Array

## Problem Statement

Given a **sorted array** `nums` and a target value `target`, find the **first (leftmost)** and **last (rightmost)** position of the target.

Return the result as:

```python
[first_index, last_index]
```

If the target is not found, return:

```python
[-1, -1]
```

You must write an algorithm with **O(log n)** time complexity.

---

## Example

Input:

```python
nums = [5, 7, 7, 8, 8, 10]
target = 8
```

Output:

```python
[3, 4]
```

---

Input:

```python
nums = [5, 7, 7, 8, 8, 10]
target = 6
```

Output:

```python
[-1, -1]
```

---

## Intuition

A normal binary search finds **any occurrence**.

But we need:

* First occurrence → move left even after finding target
* Last occurrence → move right even after finding target

So we perform **two binary searches**:

1. Left boundary search
2. Right boundary search

This is closely related to:

```python
Lower Bound and Upper Bound
```

---

## Approach

We create two helper functions:

* `find_first(nums, target)`
* `find_last(nums, target)`

Then combine results.

---

## Algorithm — First Occurrence

1. Initialize:

```python
low = 0
high = n - 1
first = -1
```

2. While `low <= high`:

* Find mid
* If target found:

```python
first = mid
high = mid - 1
```

Move left to find earlier occurrence.

* Else adjust search normally.

---

## Algorithm — Last Occurrence

Same logic but move right:

```python
last = mid
low = mid + 1
```

---

## Dry Run

Array:

```python
[5, 7, 7, 8, 8, 10]
target = 8
```

First search → index 3
Last search → index 4

Result:

```python
[3, 4]
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
            high = mid - 1   # move left
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
            low = mid + 1   # move right
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last


def search_range(nums, target):
    first = find_first(nums, target)
    last = find_last(nums, target)
    return [first, last]


# Example usage
nums = [5, 7, 7, 8, 8, 10]
target = 8

print(search_range(nums, target))  # Output: [3, 4]
```

---

## Time Complexity

Two binary searches:

```python
O(log n)
```

---

## Space Complexity

```python
O(1)
```

No extra memory used.

---

## Key Learning

Important concept:

Normal binary search stops when found.

Boundary binary search continues searching to find extreme positions.

This connects directly to:

* Lower Bound
* Upper Bound
* Count Occurrences
* Search Insert Position

---

## Interview Tip

Whenever you see:

* First position
* Last position
* Range of element
* Count duplicates in sorted array

Think:

Boundary Binary Search.

---

## Related Problems

* Lower Bound and Upper Bound
* Count Occurrences in Sorted Array
* Search Insert Position
* Find Peak Element
