Fibonacci search is another searching technique designed for **sorted arrays**. It uses the Fibonacci sequence to divide the array into sections, instead of halving it like binary search. The idea is to choose probe positions based on Fibonacci numbers, which gives flexibility in how the search range shrinks.

It is especially useful when the cost of accessing memory varies (like in some storage systems), because Fibonacci search tends to access locations that move progressively from left to right without large jumps.

---

Core Idea

Fibonacci search uses Fibonacci numbers to create ranges that get smaller as the algorithm progresses. At each step:

* Compare the target with the element at an index determined by a Fibonacci number.
* Reduce the search space by moving the Fibonacci window.
* Continue until the range becomes very small.

Instead of dividing the array into equal halves (like binary search), Fibonacci search divides it into segments based on Fibonacci ratios.

---

High-Level Workflow

1. Find the smallest Fibonacci number greater than or equal to the array size.
2. Use Fibonacci numbers (fibM, fibM1, fibM2) to calculate the probe index.
3. Compare target with the element at that probe position.
4. Based on comparison:

   * Move to the left segment,
   * Or the right segment,
   * Or return the index if found.
5. If remaining Fibonacci window shrinks to 1, check last element.

---

Detailed Step-by-Step Example

Array:
[5, 8, 12, 15, 22, 30, 41, 55, 60]
Target = 30

Step 1:
Array length n = 9
Smallest Fibonacci number ≥ 9 is 13

Let:
fibM = 13
fibM1 = 8
fibM2 = 5
offset = -1

Step 2: Probe index
index = offset + fibM2 = -1 + 5 = 4
arr[4] = 22 → less than target
Move right

Update Fibonacci numbers:
fibM = fibM1 (8)
fibM1 = fibM2 (5)
fibM2 = fibM - fibM1 (3)

offset = 4

Step 3: New probe
index = offset + fibM2 = 4 + 3 = 7
arr[7] = 55 → greater than target
Move left

Update Fibonacci numbers:
fibM = fibM2 (3)
fibM1 = fibM1 - fibM2 (2)
fibM2 = fibM - fibM1 (1)

Step 4: New probe
index = offset + fibM2 = 4 + 1 = 5
arr[5] = 30 → found at index 5

---

Text-Based Flowchart

Start
→ Find smallest Fibonacci number ≥ n
→ Set offset = -1
→ While fibM > 1
→ probe = min(offset + fibM2, n-1)
→ If arr[probe] < target
→ shift right: update Fibonacci numbers and offset
→ Else if arr[probe] > target
→ shift left: update Fibonacci numbers
→ Else return probe
→ If last element equals target → return index
→ Else return -1

---

Algorithm Structure (Step Form)

1. Generate Fibonacci numbers until fibM ≥ n
2. Initialize fibM1, fibM2, offset
3. Loop while fibM > 1
4. Compute probe index
5. Compare with target and adjust Fibonacci window
6. Check last position if needed
7. Return result

---

Time and Space Complexity

Best Case: O(1)
Average Case: O(log n)
Worst Case: O(log n)
Space Complexity: O(1)

---

Properties

Works only on sorted arrays
Comparison-based and in-place
More memory-friendly than binary search in specific hardware setups
Left-to-right access pattern can be advantageous

---

When to Use

Searching in sorted arrays
Situations where memory access pattern matters
Scenarios requiring predictable and safe logarithmic time

---

When Not to Use

Data is unsorted
Binary search is simpler and often faster

---

Learning Value

Fibonacci search deepens your understanding of search interval shrinking and shows how mathematical sequences like Fibonacci numbers can guide algorithm design. It highlights different ways of partitioning search space and builds strong intuition for advanced search algorithms.
