Counting sort is a non-comparison-based sorting algorithm. Instead of comparing elements with each other, it counts how many times each value appears and then uses this information to place every element directly into its correct position in the final sorted array.

This algorithm only works when the values fall within a known and reasonably small range. Because of this restriction, counting sort is extremely fast for suitable data and is widely used as a building block inside other advanced sorting techniques like radix sort.

---

Core Idea

If you know how many times each value appears, you can calculate exactly where each value should go in the sorted array. There is no need for comparisons, swaps, or shifting. You directly map values to positions.

---

Detailed Workflow

Input example:
[4, 2, 2, 8, 3, 3, 1]

Step 1: Find the Range
First, scan the array and find the minimum and maximum values.
Minimum = 1
Maximum = 8

This tells you that all values lie in the range 1 to 8, so the counting array must be of size 8 (or 9 if you include index 0).

---

Step 2: Build the Frequency Array
Create an array where each index represents a value and the value at that index represents how many times it appears.

Value:  1 2 3 4 5 6 7 8
Count:  1 2 2 1 0 0 0 1

This means:
1 appears once
2 appears twice
3 appears twice
4 appears once
8 appears once

---

Step 3: Convert to Cumulative Count
Now modify the count array so that each position stores how many elements are less than or equal to that value.

Value:     1 2 3 4 5 6 7 8
CumCount:  1 3 5 6 6 6 6 7

This directly tells you the final index placement:
All 1s end at index 0
All 2s end at index 2
All 3s end at index 4
All 4s end at index 5
All 8s end at index 6

---

Step 4: Build the Output Array
Traverse the original array from right to left to maintain stability. For each element:

1. Look up its cumulative count value.
2. Subtract 1 to get the exact index.
3. Place the element in the output array.
4. Decrease its count.

By the end of this process, the output array is fully sorted.

---

Text-Based Flowchart

Start
→ Read input array
→ Find min and max values
→ Create count array of size (max - min + 1)
→ Count frequency of each value
→ Convert count array to cumulative count
→ Create output array
→ Traverse input array from right to left
→ Place each element into its correct position
→ Copy output array back to input
→ End

---

Algorithm Structure (Step Form)

1. Read input array
2. Find maximum and minimum values
3. Initialize count array
4. Store frequency of each element
5. Convert count array to cumulative sum
6. Initialize output array
7. Place elements into output using cumulative count
8. Copy output back to input array
9. Return sorted array

---

Time and Space Complexity

Time Complexity: O(n + k)
where n is the number of elements and k is the range of values

Space Complexity: O(n + k)
Extra space is used for the count array and output array

---

Properties

Counting sort is stable
Counting sort is not comparison-based
Counting sort is not in-place
Counting sort is extremely fast when the value range is small

---

When to Use

When data values are integers
When the value range is small compared to the number of elements
When stability is required

---

When Not to Use

When the value range is extremely large
When memory usage must be minimal
When data is not numeric

---

Learning Value

Counting sort teaches how sorting can be achieved without comparisons. It introduces the idea of frequency tables, direct placement, cumulative indexing, and stability. These concepts form the backbone of advanced algorithms like radix sort and bucket sort.

```
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)

    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        count[current - min_val] -= 1
        position = count[current - min_val]
        output[position] = current

    for i in range(len(arr)):
        arr[i] = output[i]

    return arr


if __name__ == "__main__":
    sample = [4, 2, 2, 8, 3, 3, 1]
    print("Original:", sample)
    print("Sorted:", counting_sort(sample))
```
