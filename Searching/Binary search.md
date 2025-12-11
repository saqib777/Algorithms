Binary search is one of the most efficient searching algorithms, but it only works on data that is already sorted. Instead of checking elements one by one, it repeatedly divides the search space in half. This process drastically reduces the number of comparisons, making binary search far faster than linear search for large datasets.

---

Core Idea

At each step, you look at the middle element of the current search interval:

* If it matches the target, the search ends.
* If the target is smaller, you discard the right half.
* If the target is larger, you discard the left half.

By discarding half the data each time, the algorithm reduces the problem size exponentially.

---

High-Level Workflow

1. Set two pointers: low at the start and high at the end of the array.
2. While low is less than or equal to high:
   → Compute the mid index.
   → Compare the middle element with the target.
   → If equal, return the index.
   → If the target is smaller, search the left half.
   → If the target is larger, search the right half.
3. If the loop ends without finding the target, return -1.

---

Detailed Step-by-Step Example

Array: [5, 12, 18, 25, 32, 40, 47]
Target: 32

Step 1:
low = 0, high = 6, mid = 3 → arr[mid] = 25
32 > 25 → move right

Step 2:
low = 4, high = 6, mid = 5 → arr[mid] = 40
32 < 40 → move left

Step 3:
low = 4, high = 4, mid = 4 → arr[mid] = 32
Target found at index 4.

---

Text-Based Flowchart

Start
→ low = 0, high = n - 1
→ While low ≤ high
→ mid = (low + high) // 2
→ If arr[mid] == target → return mid
→ If target < arr[mid] → high = mid - 1
→ Else → low = mid + 1
→ End While
→ Return -1
→ End

---

Algorithm Structure (Step Form)

1. Read input array and target
2. Initialize low and high pointers
3. Loop until pointers cross
4. Compute mid and compare values
5. Shift boundaries based on comparison
6. Return index or -1

---

Time and Space Complexity

Best Case: O(1)
Average Case: O(log n)
Worst Case: O(log n)
Space Complexity: O(1)

---

Properties

Binary search works only on sorted data
Binary search is extremely fast on large inputs
Binary search is deterministic and predictable
Binary search is in-place and space efficient

---

When to Use

When data is sorted
When performance matters
When searching large datasets

---

When Not to Use

When array is unsorted
When working with linked lists

---

```
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    sample = [5, 12, 18, 25, 32, 40, 47]
    target = 32

    result = binary_search(sample, target)

    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found")
```
Learning Value

Binary search builds strong understanding of pointer manipulation, algorithmic precision, and logarithmic time complexity. Mastering binary search is essential for solving advanced problems like boundary searching, peak finding, rotated array search, and binary search on answers.
