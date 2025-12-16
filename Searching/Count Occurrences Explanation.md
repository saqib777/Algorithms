Counting the number of occurrences of a target element in a sorted array is a direct extension of the first and last occurrence problem. Instead of scanning the entire array, we use binary search to locate the boundaries where the target appears and compute the count efficiently.

---

Problem Understanding

Given a sorted array that may contain duplicate values and a target element, determine how many times the target appears.

Example:
Array: [1, 2, 2, 2, 3, 4, 5]
Target: 2
Occurrences: 3

---

Core Idea

In a sorted array, all occurrences of a value appear consecutively. If you can find:

* the index of the first occurrence, and
* the index of the last occurrence,

then the total count is:

count = last_index - first_index + 1

Both indices can be found using modified binary search, keeping the overall complexity logarithmic.

---

High-Level Workflow

1. Use binary search to find the first occurrence of the target.
2. Use binary search to find the last occurrence of the target.
3. If the target does not exist, return 0.
4. Otherwise, compute the count using the boundary indices.

---

Detailed Step-by-Step Example

Array:
[1, 2, 2, 2, 3, 4, 5]
Target = 2

First occurrence search:

* Finds index 1

Last occurrence search:

* Finds index 3

Count calculation:
count = 3 - 1 + 1 = 3

---

Text-Based Flowchart

Start
→ Find first occurrence using binary search
→ If first == -1
→ Return 0
→ Find last occurrence using binary search
→ count = last - first + 1
→ Return count
→ End

---

Algorithm Structure (Step Form)

1. Read sorted array and target
2. Perform binary search to find first occurrence
3. Perform binary search to find last occurrence
4. If not found, return 0
5. Else return (last - first + 1)

---

Time and Space Complexity

Time Complexity: O(log n)
Space Complexity: O(1)

---

Properties

Works only on sorted arrays
Efficient for large datasets
Comparison-based and in-place

---

When to Use

When frequency of an element is required
When array is sorted and may contain duplicates
When performance matters

---

```
def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1


if __name__ == "__main__":
    sample = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    print("Count:", count_occurrences(sample, target))


Learning Value

```

This pattern teaches how to extract quantitative information from sorted data using boundary searches. It reinforces binary search mastery and prepares you for range queries, frequency analysis, and interval-based problems often seen in interviews and real systems.
