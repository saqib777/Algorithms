Interpolation search is an improved version of binary search designed for **uniformly distributed** sorted data. Instead of always checking the middle element like binary search, interpolation search estimates the position of the target using its value.

The logic is simple:
If values are evenly spaced, then the closer the target is to the right end, the closer its index will be to the right side of the array.

This makes interpolation search extremely fast when data is uniform.

---

Core Idea

Binary search splits the array exactly in the middle.
Interpolation search predicts where the target might be based on its value:

Estimated Position = low + ((target - arr[low]) × (high - low)) / (arr[high] - arr[low])

This is similar to how you search words in a dictionary:
You don’t open the exact middle—you jump closer to where the word should be.

---

High-Level Workflow

1. Check if the target is within array bounds.
2. While low ≤ high and target is within arr[low] and arr[high]:
   → Estimate the probable mid position.
   → If arr[mid] == target → return mid.
   → If target < arr[mid] → search left.
   → If target > arr[mid] → search right.
3. If search ends → return -1.

---

Detailed Step-by-Step Example

Array (uniformly spaced):
[10, 20, 30, 40, 50, 60, 70]
Target = 50

Step 1:
low = 0, high = 6
Estimate mid:
mid = 0 + (50 - 10) × (6 - 0) / (70 - 10)
mid = 0 + (40 × 6) / 60
mid = 4
arr[4] = 50 → found.

This is why interpolation search can find elements in **O(1)** when distribution is uniform.

---

Text-Based Flowchart

Start
→ low = 0, high = n - 1
→ While low ≤ high AND target within range
→ mid = low + ((target - arr[low]) × (high - low) / (arr[high] - arr[low]))
→ If arr[mid] == target → return mid
→ If target < arr[mid] → high = mid - 1
→ Else → low = mid + 1
→ Return -1
→ End

---

Algorithm Structure (Step Form)

1. Initialize low and high
2. While search space is valid and data range matches
3. Estimate mid using interpolation formula
4. Compare arr[mid] with target
5. Adjust search boundaries
6. Return index or -1

---

Time and Space Complexity

Best Case: O(1)
Average Case: O(log log n)
Worst Case: O(n) (when data is not uniform)

Space Complexity: O(1)

---

Properties

Interpolation search requires sorted **and nearly uniform** data
Faster than binary search on uniform datasets
Slower on clustered or skewed data
Comparison-based and in-place

---

When to Use

Data is sorted
Data is uniformly distributed (e.g., IDs, temperatures, sequential logs)
Looking for better-than-binary-search performance

---

When Not to Use

Data distribution is unknown or skewed
Linked lists (no random access)
Worst-case behavior must be predictable

---

Learning Value

Interpolation search teaches how mathematical estimation can improve search efficiency. It introduces the concept of adaptive searching, where the search strategy adjusts based on the data distribution. Understanding interpolation search is key to grasping how real-world systems optimize lookups using value-based heuristics.
