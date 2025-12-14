Finding the ceiling and floor of a value in a sorted array is another important binary search variant. Instead of searching for an exact match, the goal is to find the closest values relative to the target.

---

Problem Understanding

Given a sorted array and a target value:

* Floor of x is the greatest element less than or equal to x
* Ceiling of x is the smallest element greater than or equal to x

Example:
Array: [1, 3, 5, 7, 9]
Target = 6
Floor = 5
Ceiling = 7

---

Core Idea

Binary search is adapted so that even when the target is not found, we keep track of the best possible candidates for floor and ceiling while narrowing the search range.

---

High-Level Workflow

1. Initialize low = 0, high = n - 1
2. While low ≤ high
   → Compute mid
   → If arr[mid] == target
   → Floor and ceiling are both arr[mid]
   → If arr[mid] < target
   → arr[mid] is a floor candidate
   → Move right
   → If arr[mid] > target
   → arr[mid] is a ceiling candidate
   → Move left
3. When loop ends, return stored floor and ceiling values

---

Detailed Step-by-Step Example

Array:
[1, 3, 5, 7, 9]
Target = 6

low = 0, high = 4
mid = 2 → arr[2] = 5
5 < 6 → floor = 5
Move right

low = 3, high = 4
mid = 3 → arr[3] = 7
7 > 6 → ceiling = 7
Move left

low = 3, high = 2 → loop ends

Final result:
Floor = 5
Ceiling = 7

---

Text-Based Flowchart

Start
→ low = 0, high = n - 1
→ While low ≤ high
→ mid = (low + high) // 2
→ If arr[mid] == target
→ floor = ceiling = arr[mid]
→ break
→ If arr[mid] < target
→ floor = arr[mid]
→ low = mid + 1
→ Else
→ ceiling = arr[mid]
→ high = mid - 1
→ End
→ Return floor and ceiling

---

Algorithm Structure (Step Form)

1. Read sorted array and target
2. Initialize floor = None, ceiling = None
3. Perform modified binary search
4. Update floor or ceiling candidates
5. Return results

---

Time and Space Complexity

Time Complexity: O(log n)
Space Complexity: O(1)

---

Properties

Works only on sorted arrays
Handles missing target values
Efficient and deterministic

---

When to Use

When closest values are required
When range-based queries are needed
When preparing frequency or bucket logic

---

Learning Value

This pattern strengthens boundary handling in binary search. It trains you to think beyond exact matches and extract relational information from sorted data, a key skill for interval problems and advanced searching techniques.
