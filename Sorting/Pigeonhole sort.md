Pigeonhole sort is a sorting algorithm that works on the idea of placing elements into specific “holes” (or buckets) based on their value. It is very similar in spirit to counting sort, but instead of counting frequencies, it directly stores values into dedicated positions. This makes it extremely fast when the range of input values is small.

---

Core Idea

If you know that all values lie within a small range, you can create one slot (pigeonhole) for every possible value. Then you place each element directly into its corresponding slot. Finally, you collect the values from the slots in order. This directly produces a sorted result without comparisons.

---

High-Level Workflow

1. Find the minimum and maximum values in the array.
2. Create a list of empty pigeonholes for the full value range.
3. Place each element into its corresponding pigeonhole.
4. Traverse the pigeonholes in order and collect the elements.

---

Detailed Step-by-Step Example

Input array:
[8, 3, 2, 7, 4, 6, 8]

Step 1: Find Range
Minimum = 2
Maximum = 8
Range = 7

Step 2: Create Pigeonholes
Create 7 empty lists for values 2 through 8

Step 3: Place Elements
Value 8 → hole 6
Value 3 → hole 1
Value 2 → hole 0
Value 7 → hole 5
Value 4 → hole 2
Value 6 → hole 4
Value 8 → hole 6 again

Step 4: Collect in Order
Traverse holes from smallest to largest and rebuild the array:
[2, 3, 4, 6, 7, 8, 8]

---

Text-Based Flowchart

Start
→ Read input array
→ Find min and max values
→ Create pigeonholes for full range
→ For each element, place into its hole
→ Traverse holes and rebuild array
→ End

---

Algorithm Structure (Step Form)

1. Read input array
2. Find minimum and maximum values
3. Create a list of empty lists for pigeonholes
4. Insert each element into its mapped pigeonhole
5. Traverse pigeonholes in order
6. Copy values back to the original array
7. Return sorted array

---

Time and Space Complexity

Time Complexity: O(n + k)
Where n is the number of elements and k is the value range

Space Complexity: O(n + k)
Extra memory is used for pigeonholes

---

Properties

Pigeonhole sort is stable
Pigeonhole sort is not comparison-based
Pigeonhole sort is not in-place
Pigeonhole sort is extremely fast for small value ranges

---

When to Use

When value range is small
When input values are integers
When duplicates are expected

---

When Not to Use

When value range is very large
When memory usage must be minimal

---

Learning Value

Pigeonhole sort helps you understand direct addressing, range-based sorting, and how eliminating comparisons can drastically improve speed when constraints are favorable. It also deepens understanding of how counting sort and bucket-style algorithms relate.

```
def pigeonhole_sort(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1

    holes = [[] for _ in range(size)]

    for value in arr:
        holes[value - min_val].append(value)

    index = 0
    for hole in holes:
        for value in hole:
            arr[index] = value
            index += 1

    return arr


if __name__ == "__main__":
    sample = [8, 3, 2, 7, 4, 6, 8]
    print("Original:", sample)
    print("Sorted:", pigeonhole_sort(sample))

```
