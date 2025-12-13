Searching in a rotated sorted array is a classic variation of binary search. The array was originally sorted in ascending order, but then rotated at some unknown pivot. Despite the rotation, the array still contains a lot of structure that we can exploit to search efficiently.

---

Problem Understanding

A rotated sorted array looks like this:
Original sorted array:
[1, 2, 3, 4, 5, 6, 7]

After rotation:
[4, 5, 6, 7, 1, 2, 3]

Even though the array is not fully sorted anymore, one important property always holds:
At least one half of the array is sorted.

---

Core Idea

At every step of binary search:

* Find the middle element.
* Check which half (left or right) is sorted.
* Decide whether the target lies in the sorted half or the unsorted half.
* Discard the half where the target cannot exist.

This keeps the time complexity logarithmic.

---

High-Level Workflow

1. Initialize low = 0, high = n - 1.
2. While low ≤ high:
   → Compute mid.
   → If arr[mid] == target, return mid.
   → Check if left half is sorted.
   → If target lies in left half, move high.
   → Else move low.
   → Otherwise, right half is sorted.
   → If target lies in right half, move low.
   → Else move high.
3. If loop ends, target is not present.

---

Detailed Step-by-Step Example

Array:
[4, 5, 6, 7, 0, 1, 2]
Target = 0

Step 1:
low = 0, high = 6
mid = 3 → arr[3] = 7
Left half [4,5,6,7] is sorted.
Target 0 is not in left half.
Move low to mid + 1.

Step 2:
low = 4, high = 6
mid = 5 → arr[5] = 1
Left half [0,1] is sorted.
Target 0 lies in this range.
Move high to mid - 1.

Step 3:
low = 4, high = 4
mid = 4 → arr[4] = 0
Target found at index 4.

---

Text-Based Flowchart

Start
→ low = 0, high = n - 1
→ While low ≤ high
→ mid = (low + high) // 2
→ If arr[mid] == target → return mid
→ If left half is sorted
→ If target in left range → high = mid - 1
→ Else → low = mid + 1
→ Else right half is sorted
→ If target in right range → low = mid + 1
→ Else → high = mid - 1
→ Return -1
→ End

---

Algorithm Structure (Step Form)

1. Read rotated sorted array and target
2. Initialize low and high pointers
3. Loop while low ≤ high
4. Find mid
5. Identify sorted half
6. Narrow search range
7. Return index or -1

---

Time and Space Complexity

Time Complexity: O(log n)
Space Complexity: O(1)

---

Properties

Works only if array was originally sorted
Handles rotation at any pivot
Comparison-based and in-place
Efficient and interview-critical

---

When to Use

Searching in rotated arrays
Interview problems involving pivoted data
When logarithmic performance is required

---

```

def search_rotated_sorted_array(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


if __name__ == "__main__":
    sample = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    result = search_rotated_sorted_array(sample, target)

    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found")

```
Learning Value

This problem teaches how to preserve efficiency even when data structure constraints change. It strengthens reasoning about invariants, conditional logic, and binary search adaptations. Mastering this pattern unlocks many advanced interview problems.
