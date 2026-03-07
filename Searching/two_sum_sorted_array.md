
# Two Sum in a Sorted Array — The Power of Two Pointers

Sometimes the simplest optimization comes from looking at a problem from both ends at once.

The **Two Pointers technique** is a perfect example of this idea. Instead of checking every possible pair of numbers, we use two pointers that move toward each other based on conditions.

One of the most classic problems that demonstrates this idea is **Two Sum in a Sorted Array**.

---

## The Problem

You are given a **sorted array** of integers `nums` and a target value `target`.

Your task is to find two numbers such that:

```
nums[i] + nums[j] = target
```

Return the indices of the two numbers.

Example:

```
nums = [2,7,11,15]
target = 9
```

Output:

```
[0,1]
```

Because:

```
2 + 7 = 9
```

---

## Naive Approach

The brute-force method is simple.

Check every pair:

```
for i:
    for j:
        if nums[i] + nums[j] == target
```

Time complexity:

```
O(n²)
```

This becomes slow for large arrays.

But since the array is **sorted**, we can do much better.

---

## The Two Pointer Insight

Place two pointers:

Left pointer at the start
Right pointer at the end

Example:

```
[2,7,11,15]
 L       R
```

Now check the sum.

If the sum is **too small**, move the left pointer right.

If the sum is **too large**, move the right pointer left.

This works because the array is sorted.

---

## Why This Works

If:

```
nums[left] + nums[right] < target
```

Then increasing the left pointer increases the sum.

If:

```
nums[left] + nums[right] > target
```

Then decreasing the right pointer decreases the sum.

This eliminates one element from consideration every step.

---

## Algorithm

1. Initialize two pointers

```
left = 0
right = n - 1
```

2. While `left < right`

3. Compute the sum

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

print(two_sum_sorted(nums, 9))  # [0,1]
```

---

## Time Complexity

The pointers move at most `n` times.

```
O(n)
```

---

## Space Complexity

No extra memory is used.

```
O(1)
```

---

## Why This Pattern Matters

The Two Pointers technique appears in many problems, including:

* Remove duplicates from sorted array
* Container with most water
* 3Sum problem
* Trapping rain water
* Pair difference problems

Once you recognize the pattern, many problems become dramatically simpler.
