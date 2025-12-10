Intro sort (Introspective Sort) is a hybrid sorting algorithm designed to combine the fast average-case performance of quick sort with the guaranteed worst-case performance of heap sort, and the efficiency of insertion sort on small arrays. It starts with quick sort and dynamically switches strategies when it detects that recursion is going too deep.

---

Core Idea

Quick sort is extremely fast on average but can degrade to O(n²) in the worst case if bad pivots are chosen repeatedly. Intro sort avoids this risk by monitoring the recursion depth. If the depth exceeds a safe limit (based on log₂(n)), it abandons quick sort and switches to heap sort, which guarantees O(n log n) performance. For very small subarrays, it uses insertion sort for maximum efficiency.

In simple words:

* Start with quick sort
* If recursion goes too deep → switch to heap sort
* If subarray is very small → use insertion sort

---

High-Level Workflow

1. Compute a maximum allowed recursion depth = 2 × log₂(n)
2. Start sorting using quick sort
3. If the recursion depth exceeds the limit → switch to heap sort
4. If the subarray size becomes very small → use insertion sort
5. Continue until the entire array is sorted

---

Why Intro Sort Exists

Quick sort is fast but risky in the worst case.
Heap sort is safe in the worst case but usually slower than quick sort.
Insertion sort is very fast on tiny arrays.

Intro sort intelligently combines all three so you get:

* Quick sort speed
* Heap sort safety
* Insertion sort efficiency

---

Text-Based Flowchart

Start
→ Compute depth_limit = 2 × log₂(n)
→ Call intro_sort_util(arr, depth_limit)

intro_sort_util(arr, depth_limit):
→ If size of arr < threshold
→ Use insertion sort
→ Return
→ If depth_limit == 0
→ Use heap sort
→ Return
→ Partition using quick sort
→ Recursively apply intro_sort_util on left and right partitions

---

Algorithm Structure (Step Form)

1. Read input array
2. Compute depth limit using log₂(n)
3. Call recursive intro sort function
4. If subarray is small, use insertion sort
5. If depth limit is exhausted, use heap sort
6. Otherwise, partition like quick sort
7. Recurse on left and right subarrays
8. Return sorted array

---

Time and Space Complexity

Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)

Space Complexity: O(log n) due to recursion stack

---

Properties

Intro sort is not stable
Intro sort is in-place
Intro sort is comparison-based
Intro sort is adaptive
Intro sort has guaranteed worst-case performance

---

When to Use

When both speed and worst-case guarantees are required
When implementing standard library sorting
When working with large datasets

---

When Not to Use

When a stable sort is strictly required
When implementing very simple educational sorting examples

---

Learning Value

Intro sort teaches how real-world production algorithms are engineered for both speed and safety. It shows how multiple algorithms can be layered intelligently to eliminate weaknesses and preserve strengths. Understanding intro sort means you now understand how modern language-level sorting functions are designed internally.

```
import math


def insertion_sort_range(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def heapify_range(arr, n, i, offset):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[offset + left] > arr[offset + largest]:
        largest = left

    if right < n and arr[offset + right] > arr[offset + largest]:
        largest = right

    if largest != i:
        arr[offset + i], arr[offset + largest] = arr[offset + largest], arr[offset + i]
        heapify_range(arr, n, largest, offset)


def heap_sort_range(arr, left, right):
    n = right - left + 1

    for i in range(n // 2 - 1, -1, -1):
        heapify_range(arr, n, i, left)

    for i in range(n - 1, 0, -1):
        arr[left], arr[left + i] = arr[left + i], arr[left]
        heapify_range(arr, i, 0, left)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def intro_sort_util(arr, low, high, depth_limit):
    size = high - low + 1

    if size < 16:
        insertion_sort_range(arr, low, high)
        return

    if depth_limit == 0:
        heap_sort_range(arr, low, high)
        return

    pivot_index = partition(arr, low, high)
    intro_sort_util(arr, low, pivot_index - 1, depth_limit - 1)
    intro_sort_util(arr, pivot_index + 1, high, depth_limit - 1)


def intro_sort(arr):
    n = len(arr)
    depth_limit = 2 * int(math.log2(n)) if n > 0 else 0
    intro_sort_util(arr, 0, n - 1, depth_limit)
    return arr


if __name__ == "__main__":
    sample = [24, 97, 40, 67, 88, 85, 15, 66, 53, 44, 26, 48, 16, 52]
    print("Original:", sample)
    print("Sorted:", intro_sort(sample))
```


