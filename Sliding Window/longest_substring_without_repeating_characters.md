
# Maximum Sum Subarray of Size K — Introduction to Sliding Window

When working with arrays, a common problem is to find the best subarray (continuous segment) that satisfies some condition.

A brute force approach often leads to nested loops and poor performance.

This is where the **Sliding Window technique** becomes powerful.

---

## The Problem

Given an array `nums` and an integer `k`, find the **maximum sum of any contiguous subarray of size k**.

Example:

```id="wq1l2a"
nums = [2, 1, 5, 1, 3, 2]
k = 3
```

Output:

```id="nq8yfz"
9
```

Explanation:

Subarrays of size 3:

```id="5q2f8g"
[2,1,5] → 8  
[1,5,1] → 7  
[5,1,3] → 9  
[1,3,2] → 6
```

Maximum = 9

---

## Brute Force Approach

Check every subarray of size `k`.

```id="r2m4v8"
for i in range(n-k+1):
    sum(nums[i:i+k])
```

Time Complexity:

```id="2x5l9c"
O(n * k)
```

This becomes inefficient when `k` is large.

---

## Sliding Window Idea

Instead of recalculating the sum every time, we reuse previous results.

We maintain a **window of size k** and slide it across the array.

Key idea:

* Add the next element
* Remove the previous element

---

## Visualization

```id="3pq7kx"
[2, 1, 5, 1, 3, 2]
  -----
```

Move window →

```id="c4x8y9"
   -----
```

Each step updates the sum in constant time.

---

## Algorithm

1. Calculate sum of first `k` elements
2. Store it as current and maximum sum
3. Slide the window:

   * Add next element
   * Subtract element leaving window
4. Update maximum

---

## Python Implementation

```python id="m1z8qe"
def max_sum_subarray(nums, k):

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):

        window_sum += nums[i]
        window_sum -= nums[i - k]

        max_sum = max(max_sum, window_sum)

    return max_sum


# Example
nums = [2, 1, 5, 1, 3, 2]

print(max_sum_subarray(nums, 3))
```

Output:

```id="7q1pzx"
9
```

---

## Time Complexity

We traverse the array once.

```id="6k2j8d"
O(n)
```

---

## Space Complexity

```id="9m3t1r"
O(1)
```

---

## Why This Problem Matters

This problem introduces the **Sliding Window pattern**, which is widely used in:

* Subarray problems
* String problems
* Longest/shortest window problems
* Frequency tracking

Once you understand this, you can move to more advanced problems like:

* Longest Substring Without Repeating Characters
* Minimum Window Substring
* Maximum Sum Subarray (variable size)
