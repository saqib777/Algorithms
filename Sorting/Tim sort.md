Tim sort is a hybrid sorting algorithm that combines the strengths of insertion sort and merge sort. It is the default sorting algorithm used in Python and Java because of its excellent real-world performance on practical data sets.

---

Core Idea

Tim sort is built on two key observations about real-world data:

1. Real data is often partially sorted.
2. Small arrays are sorted very efficiently using insertion sort.

Tim sort first breaks the array into small sorted chunks called runs. These runs are sorted using insertion sort. Then, these sorted runs are merged together using a merge sort–style process. This way, Tim sort gets the speed of insertion sort on small or nearly sorted data and the efficiency of merge sort on large datasets.

---

High-Level Workflow

1. Divide the array into small segments called runs.
2. Sort each run using insertion sort.
3. Repeatedly merge runs together using merge logic.
4. Continue merging until only one fully sorted array remains.

---

What is a Run?

A run is a small subarray that is already sorted or made sorted. Tim sort usually uses a minimum run size between 32 and 64 elements. This size is chosen because insertion sort performs extremely well on arrays of this size.

---

Detailed Step-by-Step Example

Input array:
[5, 21, 7, 23, 19, 10, 14, 3, 8, 2]

Assume run size = 4

Step 1: Break into runs
Run 1 → [5, 21, 7, 23]
Run 2 → [19, 10, 14, 3]
Run 3 → [8, 2]

Step 2: Sort each run using insertion sort
Run 1 → [5, 7, 21, 23]
Run 2 → [3, 10, 14, 19]
Run 3 → [2, 8]

Step 3: Merge runs
Merge Run 1 and Run 2 → [3, 5, 7, 10, 14, 19, 21, 23]
Merge the result with Run 3 → [2, 3, 5, 7, 8, 10, 14, 19, 21, 23]

Final sorted array is obtained.

---

Text-Based Flowchart

Start
→ Find minimum run size
→ Divide array into runs
→ Sort each run using insertion sort
→ Merge runs using merge logic
→ Repeat merging until one run remains
→ End

---

Algorithm Structure (Step Form)

1. Read input array
2. Compute minimum run length
3. For every run-sized segment
   → Sort using insertion sort
4. Merge adjacent runs
5. Continue merging until fully sorted
6. Return sorted array

---

Time and Space Complexity

Best Case: O(n)
Average Case: O(n log n)
Worst Case: O(n log n)

Space Complexity: O(n)
Extra space is required for merging operations

---

Properties

Tim sort is stable
Tim sort is adaptive
Tim sort is comparison-based
Tim sort is not in-place

---

When to Use

When sorting real-world data
When data is partially sorted
When stability is required

---

When Not to Use

When memory usage must be strictly minimal
When implementing very low-level embedded systems

---

Learning Value

Tim sort teaches how real-world algorithms are engineered using hybrid strategies. It demonstrates that combining multiple simple algorithms can create a highly optimized and production-ready solution.

```
def insertion_sort_for_timsort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def tim_sort(arr):
    n = len(arr)
    min_run = 32

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_for_timsort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

    return arr


if __name__ == "__main__":
    sample = [5, 21, 7, 23, 19, 10, 14, 3, 8, 2]
    print("Original:", sample)
    print("Sorted:", tim_sort(sample))

```
