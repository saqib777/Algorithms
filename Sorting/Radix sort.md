Radix sort is a non-comparison-based sorting algorithm that sorts numbers digit by digit, instead of comparing entire values at once. It works by processing the least significant digit first and moving towards the most significant digit. Because it relies on digit positions, radix sort is especially efficient for large lists of integers with a fixed number of digits.

---

Core Idea

Instead of sorting numbers directly, radix sort groups numbers based on individual digit positions. At each stage, numbers are placed into buckets according to the current digit being processed. After processing all digit positions, the numbers end up fully sorted.

---

High-Level Workflow

1. Find the maximum number in the array to determine how many digits need to be processed.
2. Start with the least significant digit (units place).
3. Sort the numbers based on that digit using a stable sub-sorting method, usually counting sort.
4. Move to the next digit (tens, hundreds, and so on).
5. Repeat until all digits of the largest number have been processed.

---

Detailed Step-by-Step Example

Input array:
[170, 45, 75, 90, 802, 24, 2, 66]

Pass 1: Sort by units digit
Digits: [0,5,5,0,2,4,2,6]
After sorting by units digit:
[170, 90, 802, 2, 24, 45, 75, 66]

Pass 2: Sort by tens digit
Digits: [7,9,0,0,2,4,7,6]
After sorting by tens digit:
[802, 2, 24, 45, 66, 170, 75, 90]

Pass 3: Sort by hundreds digit
Digits: [8,0,0,0,0,1,0,0]
After sorting by hundreds digit:
[2, 24, 45, 66, 75, 90, 170, 802]

Final sorted array is obtained after the last digit is processed.

---

Text-Based Flowchart

Start
→ Find the maximum number
→ Set digit place to 1
→ While max_value / digit_place > 0
→ Perform counting sort based on current digit
→ Move to next digit place (multiply by 10)
→ End

---

Algorithm Structure (Step Form)

1. Read the input array
2. Find the maximum value
3. For digit_place = 1, 10, 100, ... while max_value / digit_place > 0
   a. Apply stable counting sort based on digit_place
4. Return the sorted array

---

Time and Space Complexity

Time Complexity: O(d × (n + k))
Where:
n = number of elements
k = range of digit values (0–9)
d = number of digits in the largest number

Space Complexity: O(n + k)
Extra space is used for the output and count arrays

---

Properties

Radix sort is stable
Radix sort is not comparison-based
Radix sort is not in-place
Radix sort is extremely fast for large datasets with fixed-length integers

---

When to Use

When sorting large numbers of integers
When all numbers have limited digits
When stable sorting is required

---

When Not to Use

When numbers have very large digit lengths
When memory is highly constrained
When sorting floating-point or mixed data types

---

Learning Value

Radix sort reinforces the idea that sorting does not always require comparisons. It strengthens understanding of place value, stability, and how layered sorting can solve complex problems efficiently. It also builds directly on top of counting sort, making it a natural next step in your learning sequence.
