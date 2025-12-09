Comb sort is an improved version of bubble sort that solves its biggest weakness: slow movement of small values from the end of the list to the beginning. Bubble sort only swaps adjacent elements, which makes it very slow when a very small number is stuck far to the right. Comb sort fixes this by allowing comparisons and swaps at larger gaps, which shrink over time.

---

Core Idea

Comb sort works by comparing elements that are a certain gap apart instead of only adjacent elements. This gap starts large and keeps shrinking after every pass. As the gap becomes smaller, the algorithm slowly turns into bubble sort. By the time the gap reaches 1, most of the disorder in the array has already been removed, making the final bubble-like phase very fast.

---

High-Level Workflow

1. Initialize the gap as the size of the array.
2. Reduce the gap using a shrink factor (commonly 1.3).
3. Compare and swap elements that are gap distance apart.
4. If any swaps occur, repeat.
5. Continue until gap becomes 1 and no swaps occur.

---

Why Comb Sort is Faster Than Bubble Sort

Bubble sort suffers from the problem of turtles (small values moving very slowly to the front). Comb sort eliminates turtles early by using large gaps first. This drastically reduces the total number of swaps needed.

---

Detailed Step-by-Step Example

Input array:
[8, 4, 1, 56, 3, 44, 23]

Initial gap = 7
Shrink factor = 1.3
New gap = 7 / 1.3 ≈ 5
Compare:
8 and 44 → swap
4 and 23 → no swap
Array becomes:
[44, 4, 1, 56, 3, 8, 23]

Next gap = 5 / 1.3 ≈ 3
Compare:
44 and 56 → no swap
4 and 3 → swap
1 and 8 → no swap
Array becomes:
[44, 3, 1, 56, 4, 8, 23]

Next gap = 3 / 1.3 ≈ 2
Compare:
44 and 1 → swap
3 and 56 → no swap
1 and 4 → no swap
56 and 8 → swap
Array becomes:
[1, 3, 44, 8, 4, 56, 23]

Eventually gap becomes 1 and the array is finalized using a fast bubble pass.

---

Text-Based Flowchart

Start
→ Set gap = array length
→ Set swapped = True
→ While gap > 1 OR swapped is True
→ gap = gap / 1.3
→ if gap < 1, gap = 1
→ swapped = False
→ For i from 0 to n - gap
→ If arr[i] > arr[i + gap]
→ Swap
→ swapped = True
→ End

---

Algorithm Structure (Step Form)

1. Read input array
2. Set gap = length of array
3. Set swapped = true
4. While gap > 1 or swapped is true
   → gap = gap / 1.3
   → if gap < 1 then gap = 1
   → swapped = false
   → For i from 0 to n - gap - 1
   → if arr[i] > arr[i + gap]
   → swap
   → swapped = true
5. Return sorted array

---

Time and Space Complexity

Best Case: O(n log n)
Average Case: O(n² / 2^p) (much faster than bubble sort in practice)
Worst Case: O(n²)

Space Complexity: O(1)

---

Properties

Comb sort is not stable
Comb sort is in-place
Comb sort is comparison-based
Comb sort is much faster than bubble sort

---

When to Use

When you want a simple improvement over bubble sort
When memory must remain constant
When teaching optimization concepts

---

Learning Value

Comb sort clearly demonstrates how a small change in strategy (gap-based comparison) can produce large performance improvements. It strengthens understanding of optimization, gap sequences, and algorithm tuning.
