Linear search is the simplest searching algorithm. It works by checking each element of the list one by one until the target value is found or the list ends. It does not require the data to be sorted, which makes it very flexible and easy to use.

---

Core Idea

Start from the first element and move forward step by step. At each step, compare the current element with the target value. If they match, stop immediately. If the end of the list is reached without a match, the element does not exist in the list.

---

High-Level Workflow

1. Start from the first element.
2. Compare it with the target value.
3. If it matches, return the index.
4. If it does not match, move to the next element.
5. Repeat until the list ends.
6. If no match is found, return -1.

---

Detailed Step-by-Step Example

Input array:
[10, 25, 30, 45, 50]
Target value: 45

Comparison steps:
10 ≠ 45 → move forward
25 ≠ 45 → move forward
30 ≠ 45 → move forward
45 = 45 → found at index 3

The search stops immediately when the match is found.

---

Text-Based Flowchart

Start
→ Take input array and target
→ Set index = 0
→ While index < length of array
→ If array[index] == target
→ Return index (found)
→ Else
→ index = index + 1
→ End While
→ Return -1 (not found)
→ End

---

Algorithm Structure (Step Form)

1. Read input array and target value
2. For each element in the array
   → Compare with target
   → If equal, return index
3. If loop ends, return -1

---

Time and Space Complexity

Best Case: O(1) (element found at first position)
Average Case: O(n)
Worst Case: O(n) (element not found or at the last position)

Space Complexity: O(1)

---

Properties

Linear search works on both sorted and unsorted arrays
Linear search is stable and does not modify data
Linear search is not efficient for large datasets

---

When to Use

When the list is small
When the data is unsorted
When simplicity is more important than speed

---

When Not to Use

When the list is very large
When fast searching is required

---

Learning Value

Linear search builds the foundation for all searching techniques. It strengthens your understanding of traversal, comparisons, and basic algorithmic flow. Every advanced searching algorithm is built as an optimization of this basic idea.

```

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


if __name__ == "__main__":
    sample = [10, 25, 30, 45, 50]
    target = 45

    result = linear_search(sample, target)

    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found")

```
