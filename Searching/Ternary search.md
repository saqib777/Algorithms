Ternary search is a divide‑and‑conquer searching algorithm similar to binary search, but instead of splitting the search interval into two parts, it divides it into three. This means that at every step, the algorithm evaluates two midpoints instead of one. Based on comparisons with these midpoints, it eliminates one‑third of the search space each time.

Important Note: Ternary search is primarily used on *unimodal functions* (functions that increase and then decrease, or vice‑versa). When applied to sorted arrays, it works correctly but is **not** more efficient than binary search. In fact, binary search is mathematically faster despite using fewer comparisons.

---

Core Idea

1. Divide the current range into three equal parts.
2. Compare the target value with two midpoints.
3. Determine which of the three segments the target could lie in.
4. Recursively or iteratively search only that segment.

---

High‑Level Workflow

Given low and high indices:

1. Compute mid1 = low + (high - low) // 3
2. Compute mid2 = high - (high - low) // 3
3. If arr[mid1] == target → return mid1
4. If arr[mid2] == target → return mid2
5. If target < arr[mid1] → search in [low, mid1 - 1]
6. Else if target > arr[mid2] → search in [mid2 + 1, high]
7. Else → search in [mid1 + 1, mid2 - 1]

---

Detailed Step‑By‑Step Example

Array:
[3, 9, 12, 17, 25, 31, 42, 56]
Target = 25

Step 1:
low = 0, high = 7
mid1 = 2 → arr[2] = 12
mid2 = 5 → arr[5] = 31

Target (25) lies between 12 and 31 → search [3, 4]

Step 2:
Now low = 3, high = 4
mid1 = 3 → arr[3] = 17
mid2 = 4 → arr[4] = 25
Target found at index 4.

---

Text‑Based Flowchart

Start
→ low = 0, high = n - 1
→ While low ≤ high
→ mid1 = low + (high - low) // 3
→ mid2 = high - (high - low) // 3
→ If arr[mid1] == target → return mid1
→ If arr[mid2] == target → return mid2
→ If target < arr[mid1] → high = mid1 - 1
→ Else if target > arr[mid2] → low = mid2 + 1
→ Else → low = mid1 + 1, high = mid2 - 1
→ Return -1

---

Algorithm Structure (Step Form)

1. Initialize low and high
2. Loop while range is valid
3. Compute mid1 and mid2
4. Compare with midpoints
5. Shrink the search boundary accordingly
6. Return index or -1

---

Time and Space Complexity

Time Complexity: O(log₃ n), but effectively slower than binary search due to extra comparisons
Space Complexity: O(1) for iterative version

---

Properties

Ternary search requires sorted data
Not faster than binary search in practice
Useful for convex/unimodal function optimization
Comparison‑based, in‑place, deterministic

---

When to Use

When searching on **unimodal functions** (important in optimization problems)
When exploring algorithmic divide‑and‑conquer variations

---

When Not to Use

For standard sorted arrays (binary search is faster)
When minimizing comparisons or recursion depth

---

Learning Value

Ternary search reinforces divide‑and‑conquer logic by showing:

* how splitting into three parts works
* how midpoints guide decision-making
* how algorithmic performance depends on both structure and operations

Understanding ternary search builds confidence for advanced searching patterns and optimization algorithms.
