# 3Sum — Finding Triplets That Sum to Zero

The **3Sum problem** is one of the most well-known problems in algorithm interviews. It builds directly on the Two Pointers technique and teaches how to avoid duplicate results.

The goal is simple: find all unique triplets in an array whose sum equals zero.

Even though the problem sounds straightforward, solving it efficiently requires a clever strategy.

---

## The Problem

Given an integer array `nums`, return **all unique triplets** `[nums[i], nums[j], nums[k]]` such that:

```
nums[i] + nums[j] + nums[k] = 0
```

Conditions:

* `i ≠ j ≠ k`
* Triplets must be **unique**

Example:

```
nums = [-1,0,1,2,-1,-4]
```

Output:

```
[[-1,-1,2],[-1,0,1]]
```

---

## Brute Force Approach

The naive solution checks every possible triplet.

```
for i
   for j
      for k
```

Time complexity:

```
O(n³)
```

This becomes impractical for large inputs.

---

## Key Idea

We reduce the problem to **Two Sum**.

Steps:

1. Sort the array
2. Fix one element
3. Use two pointers to find the remaining two numbers

Sorting allows us to move pointers intelligently and skip duplicates.

---

## Why Sorting Helps

After sorting:

```
[-4,-1,-1,0,1,2]
```

We pick the first number and search for the remaining pair using the two-pointer technique.

Example:

```
Fix: -1
Now find two numbers that sum to +1
```

Because:

```
-1 + x + y = 0
x + y = 1
```

---

## Two Pointer Strategy

For each fixed element:

```
left = i + 1
right = n - 1
```

Compute:

```
current_sum = nums[i] + nums[left] + nums[right]
```

If:

```
sum < 0 → move left pointer
sum > 0 → move right pointer
sum == 0 → record triplet
```

Then move both pointers while skipping duplicates.

---

## Algorithm

1. Sort the array
2. Loop through elements
3. Skip duplicate values
4. Use two pointers for remaining elements
5. Record valid triplets

---

## Python Implementation

```python
def three_sum(nums):

    nums.sort()
    result = []

    for i in range(len(nums)):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result


# Example
nums = [-1,0,1,2,-1,-4]

print(three_sum(nums))
```

Output:

```
[[-1, -1, 2], [-1, 0, 1]]
```

---

## Time Complexity

Sorting:

```
O(n log n)
```

Two pointer search inside loop:

```
O(n²)
```

Overall:

```
O(n²)
```

---

## Space Complexity

```
O(1)
```

Excluding the output list.

---

## Why This Problem Is Important

3Sum introduces several key interview skills:

* Combining techniques (sorting + two pointers)
* Handling duplicates
* Reducing problem complexity

Once you understand this pattern, you can solve many related problems.

Examples include:

* 3Sum Closest
* 4Sum
* Pair difference problems
* Triplet counting problems
