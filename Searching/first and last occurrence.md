Finding the first and last occurrence of a target element in a sorted array is a classic binary search variation. The array may contain duplicate values, and the goal is not just to check if the target exists, but to find the exact range where it appears.

---

Problem Understanding

Given a sorted array that may contain duplicates, you are asked to find:

* The index of the first occurrence of the target
* The index of the last occurrence of the target

Example:
Array: [1, 2, 2, 2, 3, 4, 5]
Target: 2

First occurrence index = 1
Last occurrence index = 3

---

Core Idea

Binary search normally stops as soon as it finds the target. In this variation, we continue searching even after finding the target:

* For the first occurrence, we keep moving left
* For the last occurrence, we keep moving right

This preserves logarithmic performance while finding precise boundaries.

---

High-Level Workflow

First Occurrence:

1. Perform binary search
2. When target is found, store index
3. Continue searching left half

Last Occurrence:

1. Perform binary search
2. When target is found, store index
3. Continue searching right half

---

Detailed Step-by-Step Example

Array:
[1, 2, 2, 2, 3, 4, 5]
Target = 2

Finding First Occurrence:
low = 0, high = 6
mid = 3 → arr[3] = 2 (found)
Store index = 3
Move high = mid - 1

mid = 1 → arr[1] = 2 (found)
Store index = 1
Move high = mid - 1

mid = 0 → arr[0] = 1 (not target)
Search ends
First occurrence = 1

Finding Last Occurrence:
low = 0, high = 6
mid = 3 → arr[3] = 2 (found)
Store index = 3
Move low = mid + 1

mid = 5 → arr[5] = 4 (greater)
Move high = mid - 1

mid = 4 → arr[4] = 3 (greater)
Move high = mid - 1
Search ends
Last occurrence = 3

---

Text-Based Flowchart

Start
→ Run binary search
→ If target found
→ Save index
→ For first occurrence: move left
→ For last occurrence: move right
→ Continue until bounds cross
→ Return stored index
→ End

---

Algorithm Structure (Step Form)

1. Read sorted array and target
2. Initialize low and high
3. While low ≤ high
4. Compute mid
5. If arr[mid] == target
   → store index
   → move boundary
6. Else adjust boundaries normally
7. Return result

---

Time and Space Complexity

Time Complexity: O(log n)
Space Complexity: O(1)

---

Properties

Works only on sorted arrays
Handles duplicate values
Comparison-based and in-place
Very common interview pattern

---

When to Use

When duplicates exist
When range or frequency is required
When precise boundaries are needed

---

Learning Value

This pattern strengthens your understanding of binary search control flow. It teaches how small changes in loop conditions can extract richer information from sorted data. This concept directly extends to problems like counting occurrences, range queries, and boundary searches.
