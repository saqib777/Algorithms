Exponential search is a fast searching algorithm designed for **sorted arrays**. It is especially powerful when you need to find an element whose position is closer to the beginning of the array. The algorithm works in two phases:

1. **Exponential growth phase** – Find a range where the target may lie.
2. **Binary search phase** – Apply binary search inside that identified range.

This combination gives exponential search its speed advantage.

---

Core Idea

Instead of starting with the entire array, exponential search quickly finds an upper bound where the target could be. It does this by checking positions at powers of 2: 1, 2, 4, 8, 16, ... until the value at that index exceeds the target. Once the range is found, binary search is applied inside that limited segment.

This is extremely efficient when:

* the target is near the start of the array, or
* the array is infinitely long or unbounded.

---

High-Level Workflow

1. If the first element is the target → return index 0.
2. Set bound = 1.
3. While bound < n and arr[bound] ≤ target
   → bound = bound × 2
4. Perform binary search between indices:
   (bound / 2)  and  min(bound, n-1)

---

Detailed Step-by-Step Example

Array:
[3, 5, 7, 9, 12, 17, 19, 24, 31, 42]
Target = 19

Step 1: Check arr[0]
3 ≠ 19 → continue

Step 2: Exponential growth
bound = 1 → arr[1] = 5 ≤ 19 → continue
bound = 2 → arr[2] = 7 ≤ 19 → continue
bound = 4 → arr[4] = 12 ≤ 19 → continue
bound = 8 → arr[8] = 31 > 19 → stop

Target must lie between indices 4 and 8.

Step 3: Apply binary search on that range
Binary search finds 19 at index 6.

---

Text-Based Flowchart

Start
→ If arr[0] == target → return 0
→ bound = 1
→ While bound < n AND arr[bound] ≤ target
→ bound = bound × 2
→ Perform binary search from (bound/2) to min(bound, n-1)
→ Return index or -1
→ End

---

Algorithm Structure (Step Form)

1. Check first element
2. Initialize bound = 1
3. Double bound until passing target or end of array
4. Apply binary search on the identified range
5. Return result

---

Time and Space Complexity

Best Case: O(1)
Average Case: O(log n)
Worst Case: O(log n)
Space Complexity: O(1)

---

Properties

Exponential search requires sorted data
It is faster than binary search when target is near the beginning
Ideal for unbounded or very large arrays
Adaptive and efficient

---

When to Use

Data is sorted
You suspect the target is near the start
Searching in unbounded arrays (e.g., infinite streams)

---

When Not to Use

Targets are typically near the end
Data is unsorted
Memory access is costly (frequent jumps)

---

Learning Value

Exponential search reinforces two concepts:

* fast range finding through exponential jumps
* combining multiple algorithms (range search + binary search)

It is a great stepping-stone to understanding doubling strategies, unbounded searches, and hybrid algorithms.

```
import math


def binary_search_range(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    if arr[0] == target:
        return 0

    bound = 1
    while bound < n and arr[bound] <= target:
        bound *= 2

    left = bound // 2
    right = min(bound, n - 1)

    return binary_search_range(arr, left, right, target)


if __name__ == "__main__":
    sample = [3, 5, 7, 9, 12, 17, 19, 24, 31, 42]
    target = 19

    result = exponential_search(sample, target)
    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found")

```
