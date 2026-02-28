# Search in Bitonic Array

## Problem Statement

A **bitonic array** is an array that:

1. First increases strictly
2. Then decreases strictly

You are given a bitonic array `nums` and a target value `target`.

Your task is to return the index of the target if it exists, otherwise return `-1`.

You must solve it in **O(log n)** time complexity.

---

## Example

Input:

```python
nums = [1, 3, 8, 12, 4, 2]
target = 4
```

Output:

```python
4
```

Explanation:

Array increases until 12, then decreases.

Target 4 is found at index 4.

---

## Intuition

A bitonic array has two sorted parts:

Increasing part → left side
Decreasing part → right side

So the approach is:

Step 1 → Find the peak element index
Step 2 → Binary search on left side (ascending)
Step 3 → Binary search on right side (descending)

This gives overall complexity:

```python
O(log n)
```

---

## Step 1 — Find Peak Element

Peak element is the maximum element where:

```python
nums[i] > nums[i-1] and nums[i] > nums[i+1]
```

We use binary search to find it.

Logic:

If:

```python
nums[mid] < nums[mid + 1]
```

Move right → peak is on right

Else:

Move left → peak is mid or left side

---

## Step 2 — Binary Search on Left Side (Ascending)

Normal binary search from:

```python
0 → peak
```

---

## Step 3 — Binary Search on Right Side (Descending)

Binary search from:

```python
peak + 1 → n - 1
```

But comparison is reversed because array is descending.

---

## Algorithm

1. Find peak index
2. Search target in left half
3. If found → return index
4. Else search in right half
5. If found → return index
6. Else return -1

---

## Dry Run

Array:

```python
[1, 3, 8, 12, 4, 2]
target = 4
```

Peak = 12 (index 3)

Left search → not found

Right search → found at index 4

---

## Python Implementation

```python
def find_peak(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low


def binary_search(nums, target, low, high, ascending=True):

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if ascending:
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if target > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


def search_bitonic(nums, target):

    peak = find_peak(nums)

    # Search in left part
    index = binary_search(nums, target, 0, peak, True)
    if index != -1:
        return index

    # Search in right part
    return binary_search(nums, target, peak + 1, len(nums) - 1, False)


# Example usage
nums = [1, 3, 8, 12, 4, 2]
target = 4

print(search_bitonic(nums, target))  # Output: 4
```

---

## Time Complexity

Finding peak:

```python
O(log n)
```

Binary search left:

```python
O(log n)
```

Binary search right:

```python
O(log n)
```

Overall:

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

This problem combines multiple binary search ideas:

* Peak Element
* Binary Search in Ascending Array
* Binary Search in Descending Array

This is a **pattern composition problem**.

---

## Interview Tip

Whenever you see:

Array increases then decreases

Think:

1. Find peak
2. Search both sides

---

## Related Problems

* Find Peak Element
* Peak Index in Mountain Array
* Search in Rotated Sorted Array
* Order Agnostic Binary Search
