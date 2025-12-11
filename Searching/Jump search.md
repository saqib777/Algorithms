Jump search is a searching algorithm designed for sorted arrays. Instead of checking elements one by one (like linear search) or dividing the array repeatedly (like binary search), jump search moves ahead in fixed-size steps (or "jumps") to find a block where the target might lie. Once it identifies the correct block, it performs a linear search inside that block.

---

Core Idea

Jump ahead by a fixed block size until you either:

* land on the target, or
* step past the target.

Once you've passed the target, step back one block and search linearly inside that block.

The optimal jump size is √n, which minimizes total comparisons.

---

High-Level Workflow

1. Choose a block size = √n.
2. Jump by this block size through the array.
3. Stop when the current element is >= target.
4. Perform a linear search backward within that block.
5. If found, return index; otherwise return -1.

---

Detailed Step-by-Step Example

Array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
Target: 23

n = 10
Optimal jump = √10 ≈ 3

Jumps:
Check index 3 → arr[3] = 12 (less than 23) → jump again
Check index 6 → arr[6] = 38 (greater than 23)

We passed the target. The target must lie between indices 3 and 6.

Linear Search in block [4, 5, 6):
arr[4] = 16 → no
arr[5] = 23 → found at index 5

---

Text-Based Flowchart

Start
→ Compute block size = √n
→ prev = 0
→ curr = block size
→ While curr < n and arr[curr] < target
→ prev = curr
→ curr += block size
→ Perform linear search from prev to min(curr, n-1)
→ If found → return index
→ Else → return -1

---

Algorithm Structure (Step Form)

1. Compute block size = √n
2. Jump through the array in increments of block size
3. Identify the block where arr[curr] >= target
4. Perform linear search inside that block
5. Return index if found, otherwise -1

---

Time and Space Complexity

Best Case: O(1)
Average Case: O(√n)
Worst Case: O(√n)
Space Complexity: O(1)

---

Properties

Jump search requires sorted data
Faster than linear search for large arrays
Not as fast as binary search
In-place and comparison-based

---

When to Use

When data is sorted
When binary search is not suitable (e.g., due to costly random access)
When jump-based traversal fits the problem constraints

---

When Not to Use

On unsorted arrays
On linked lists (jumping is not efficient)
When strict logarithmic performance is needed (binary search is better)

---

Learning Value

Jump search introduces the idea of block-based searching and shows how clever step sizes (like √n) can dramatically reduce comparisons. It builds intuition for hybrid algorithms that balance skipping and scanning behaviors.

```
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))

    prev = 0
    curr = step

    while curr < n and arr[curr] < target:
        prev = curr
        curr += step

    for i in range(prev, min(curr, n)):
        if arr[i] == target:
            return i

    return -1


if __name__ == "__main__":
    sample = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23

    result = jump_search(sample, target)
    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found")

```
