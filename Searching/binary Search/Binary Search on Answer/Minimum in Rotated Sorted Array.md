# Finding the Minimum in a Rotated Sorted Array — Understanding the Binary Search Trick

If you’ve spent some time learning binary search, you’ve probably noticed that many problems are not about finding a number directly. Instead, they’re about exploiting **structure in sorted data**.

One classic example is the *Rotated Sorted Array* problem.

At first glance it looks confusing, because the array is not fully sorted anymore. But once you understand the structure behind it, the solution becomes surprisingly elegant.

Let’s break it down.

---

## The Problem

You are given an array that was originally sorted in ascending order, but then rotated at some pivot point.

Your goal is to find the **minimum element in the array**.

Example:

```
nums = [4, 5, 6, 7, 0, 1, 2]
```

Here the array was originally:

```
[0, 1, 2, 4, 5, 6, 7]
```

Then rotated.

The minimum element is:

```
0
```

Your task is to find this value in **O(log n)** time.

---

## Observing the Structure

A rotated sorted array actually consists of **two sorted halves**.

Example:

```
[4, 5, 6, 7, 0, 1, 2]
```

Left portion (sorted):

```
4 5 6 7
```

Right portion (sorted):

```
0 1 2
```

The **minimum element is where the rotation happens**.

So instead of scanning the entire array (which would take O(n)), we can use **binary search** to identify which half contains the minimum.

---

## Key Insight

The last element of the array gives us an important clue.

If:

```
nums[mid] > nums[high]
```

Then the minimum must be on the **right side**.

Why?

Because the mid element belongs to the larger sorted section before the rotation.

But if:

```
nums[mid] <= nums[high]
```

Then the minimum lies on the **left side**, including the current mid.

This simple comparison allows us to eliminate half of the search space every step.

---

## The Algorithm

1. Set two pointers:

```
low = 0
high = n - 1
```

2. While `low < high`:

* Calculate the middle index.
* Compare `nums[mid]` with `nums[high]`.

3. If `nums[mid] > nums[high]`
   → Minimum is on the **right side**.

4. Otherwise
   → Minimum is on the **left side**, including `mid`.

5. Continue until `low == high`.

That index contains the minimum element.

---

## Dry Run Example

Array:

```
[4, 5, 6, 7, 0, 1, 2]
```

Step 1

```
low = 0
high = 6
mid = 3
nums[mid] = 7
nums[high] = 2
```

Since:

```
7 > 2
```

The minimum must be on the **right side**.

Move:

```
low = mid + 1
```

---

Step 2

```
low = 4
high = 6
mid = 5
nums[mid] = 1
nums[high] = 2
```

Since:

```
1 <= 2
```

Minimum is on the **left side**.

Move:

```
high = mid
```

---

Step 3

```
low = 4
high = 5
mid = 4
```

Continue narrowing until:

```
low = high = 4
```

Result:

```
nums[4] = 0
```

Minimum found.

---

## Python Implementation

```python
def find_min(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[low]


# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]

print(find_min(nums))  # Output: 0
```

---

## Time Complexity

Binary search cuts the search space in half every iteration.

```
Time Complexity: O(log n)
```

---

## Space Complexity

No extra data structures are used.

```
Space Complexity: O(1)
```

---

## Why This Problem Matters

This problem is important because it teaches a deeper lesson about binary search.

Binary search is not only about searching for a number. It is about using **structure in data** to eliminate half of the possibilities.

Once you understand this idea, many advanced problems become approachable, including:

* Search in Rotated Sorted Array
* Find Peak Element
* Binary Search on Answer problems
* Mountain Array search

Learning to recognize these patterns is what separates someone who memorizes algorithms from someone who truly understands them.
