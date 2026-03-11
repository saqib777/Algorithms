# Two Sum in a Sorted Array — Understanding the Two Pointer Technique

Many algorithm problems can be solved faster once we take advantage of **sorted data**. One of the simplest and most powerful techniques used in such cases is the **Two Pointer approach**.

The classic problem that demonstrates this idea is **Two Sum in a Sorted Array**.

---

## The Problem

You are given a **sorted array** of integers `nums` and a target value `target`.

Your task is to find two numbers such that:

```
nums[i] + nums[j] = target
```

Return the **indices of the two numbers**.

Example:

```
nums = [2,7,11,15]
target = 9
```

Output:

```
[0,1]
```

Explanation:

```
2 + 7 = 9
```

---

## Brute Force Approach

The most straightforward solution is to check every pair of elements.

```
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            return [i, j]
```

Time Complexity:

```
O(n²)
```

This works, but it becomes inefficient for large arrays.

---

## Key Insight

Because the array is **already sorted**, we can use two pointers.

Place one pointer at the beginning and one at the end.

```
left = 0
right = n - 1
```

Now compute the sum.

```
current_sum = nums[left] + nums[right]
```

Three cases are possible.

If the sum equals the target → we found the answer.

If the sum is **smaller than the target**, we move the left pointer forward to increase the sum.

If the sum is **greater than the target**, we move the right pointer backward to decrease the sum.

This works because moving through a sorted array predictably changes the sum.

---

## Algorithm

1. Initialize two pointers

```
left = 0
right = len(nums) - 1
```

2. While `left < right`

3. Calculate the sum

4. If sum equals target → return indices

5. If sum is smaller → move left pointer

6. If sum is larger → move right pointer

---

## Python Implementation

```python
def two_sum_sorted(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:

        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return [-1, -1]


# Example
nums = [2,7,11,15]

print(two_sum_sorted(nums, 9))
```

Output:

```
[0,1]
```

---

## Time Complexity

Each pointer moves at most once across the array.

```
O(n)
```

---

## Space Complexity

No additional memory is used.

```
O(1)
```

---

## Why This Pattern Matters

The **Two Pointer technique** appears in many algorithm problems, especially when arrays are sorted.

Examples include:

* 3Sum
* 3Sum Closest
* Container With Most Water
* Trapping Rain Water
* Pair difference problems

Learning this pattern allows you to replace expensive nested loops with efficient linear scans.
