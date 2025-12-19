Finding the sum of elements in an array using recursion is a simple but very important exercise. It helps solidify how recursion reduces a problem step by step and how results are combined while returning from recursive calls.

---

Problem Understanding:

Given an array of integers, compute the sum of all its elements using recursion instead of loops.

Example:
Array: [1, 2, 3, 4, 5]
Sum = 15

---

Core Idea:

The sum of an array can be defined recursively as:

sum(arr, n) = arr[n-1] + sum(arr, n-1)

The problem size reduces by one element at each recursive call.

---

Base Case

When the array size becomes 0, there are no elements left to add.

sum(arr, 0) = 0

This stops the recursion.

---

Recursive Case

Take the last element of the current array segment and add it to the sum of the remaining elements.

---

Step-by-Step Execution Example

Array: [1, 2, 3, 4]

sum(arr, 4)
→ 4 + sum(arr, 3)
→ 4 + (3 + sum(arr, 2))
→ 4 + (3 + (2 + sum(arr, 1)))
→ 4 + (3 + (2 + (1 + sum(arr, 0))))
→ 4 + 3 + 2 + 1 + 0
→ 10

---

Text-Based Flowchart

Start
→ sum(arr, n)
→ Is n == 0?
→ Yes: return 0
→ No: return arr[n-1] + sum(arr, n-1)
→ End

---

Algorithm Structure (Step Form)

1. Read array and its size n
2. If n == 0, return 0
3. Otherwise, return arr[n-1] + sum(arr, n-1)

---

Time and Space Complexity

Time Complexity: O(n)
Space Complexity: O(n) due to recursion stack

---

Properties

Does not modify the array
Uses recursion instead of iteration
Simple divide-and-reduce approach

---

When to Use

For learning recursion fundamentals
When practicing recursive thinking

---

Learning Value

This problem trains you to:

* identify a clean base case
* reduce the problem size correctly
* understand how values are accumulated during recursive returns

It is a stepping stone to more complex recursive problems like array reversal, subsequences, and backtracking.

```
def sum_of_array(arr, n):
    # Base case
    if n == 0:
        return 0

    # Recursive case
    return arr[n - 1] + sum_of_array(arr, n - 1)


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5]
    print("Sum of array:", sum_of_array(sample, len(sample)))

```
