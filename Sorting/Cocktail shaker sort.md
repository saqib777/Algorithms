Cocktail shaker sort is a variation of bubble sort that works in both directions instead of just one. While bubble sort only pushes the largest elements toward the end, cocktail shaker sort also pushes the smallest elements toward the beginning in the same pass cycle. This makes it more efficient than standard bubble sort for certain types of data.

---

Core Idea

Instead of repeatedly moving in only one direction like bubble sort, cocktail shaker sort moves forward and backward through the list. In the forward pass, larger elements move to the right. In the backward pass, smaller elements move to the left. This bi-directional movement helps reduce the total number of passes needed.

---

High-Level Workflow

1. Perform a forward pass (left to right) just like bubble sort.
2. Perform a backward pass (right to left).
3. Narrow the unsorted range from both ends.
4. Repeat until no swaps occur.

---

Detailed Step-by-Step Example

Input array:
[5, 1, 4, 2, 8]

Forward pass:
(5,1) → swap → [1, 5, 4, 2, 8]
(5,4) → swap → [1, 4, 5, 2, 8]
(5,2) → swap → [1, 4, 2, 5, 8]
(5,8) → no swap

Backward pass:
(5,2) → no swap
(2,4) → swap → [1, 2, 4, 5, 8]
(4,1) → no swap

After one full cycle, both the largest and smallest values move closer to their correct positions.

---

Text-Based Flowchart

Start
→ Set start = 0, end = n - 1
→ Set swapped = True
→ While swapped is True
→ swapped = False
→ Forward pass from start to end
→ If arr[i] > arr[i+1], swap and set swapped = True
→ If no swaps, break
→ Decrease end
→ Backward pass from end to start
→ If arr[i] < arr[i-1], swap and set swapped = True
→ Increase start
→ End

---

Algorithm Structure (Step Form)

1. Read input array
2. Set start = 0 and end = n - 1
3. Set swapped = true
4. While swapped is true
   → Set swapped = false
   → Forward pass: for i from start to end - 1
   → if arr[i] > arr[i + 1], swap and set swapped = true
   → If swapped is false, break
   → Decrease end
   → Backward pass: for i from end to start + 1
   → if arr[i] < arr[i - 1], swap and set swapped = true
   → Increase start
5. Return sorted array

---

Time and Space Complexity

Best Case: O(n)
Average Case: O(n²)
Worst Case: O(n²)

Space Complexity: O(1)

---

Properties

Cocktail shaker sort is stable
Cocktail shaker sort is in-place
Cocktail shaker sort is comparison-based
Cocktail shaker sort is adaptive

---

When to Use

When data is nearly sorted
When bidirectional adjustment is useful
When teaching adaptive sorting techniques

---

When Not to Use

When working with very large datasets
When performance is critical

---

Learning Value

Cocktail shaker sort helps you understand how bidirectional passes can optimize basic algorithms. It highlights the importance of narrowing problem boundaries and making algorithms adaptive to the nature of data.

```
def cocktail_shaker_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        end -= 1
        swapped = False

        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        start += 1

    return arr


if __name__ == "__main__":
    sample = [5, 1, 4, 2, 8]
    print("Original:", sample)
    print("Sorted:", cocktail_shaker_sort(sample))

```
