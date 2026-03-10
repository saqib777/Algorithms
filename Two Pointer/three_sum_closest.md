# 3Sum Closest — Finding the Nearest Sum Using Two Pointers

After learning the classic **3Sum problem**, a natural extension is **3Sum Closest**. Instead of finding triplets that sum exactly to a target, we now want the triplet whose sum is **closest** to the target value.

This small change forces us to track how near our current sum is to the desired target.

---

## The Problem

Given an integer array `nums` and an integer `target`, find three numbers such that their sum is **closest to the target**.

Return the **sum of the three numbers**.

Example:

```
nums = [-1,2,1,-4]
target = 1
```

Output:

```
2
```

Explanation:

The sum closest to `1` is:

```
-1 + 2 + 1 = 2
```

---

## Key Idea

This problem uses the **same strategy as 3Sum**:

1. Sort the array
2. Fix one number
3. Use two pointers to search for the remaining pair

The difference is that instead of checking for a sum of zero, we measure how close the current sum is to the target.

---

## Why Sorting Helps

Sorting allows us to move pointers intelligently.

Example sorted array:

```
[-4,-1,1,2]
```

If the current sum is **too small**, we increase it by moving the left pointer.

If the sum is **too large**, we decrease it by moving the right pointer.

This allows us to gradually approach the target value.

---

## Algorithm

1. Sort the array.
2. Initialize a variable to store the closest sum.
3. Loop through the array.
4. For each element, use two pointers:

   * `left = i + 1`
   * `right = n - 1`
5. Compute the current sum.
6. Update the closest value if the difference is smaller.
7. Move pointers accordingly.

---

## Python Implementation

```python
def three_sum_closest(nums, target):

    nums.sort()
    closest = float('inf')

    for i in range(len(nums) - 2):

        left = i + 1
        right = len(nums) - 1

        while left < right:

            current_sum = nums[i] + nums[left] + nums[right]

            if abs(target - current_sum) < abs(target - closest):
                closest = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum

    return closest


# Example
nums = [-1,2,1,-4]

print(three_sum_closest(nums, 1))
```

---

## Time Complexity

Sorting:

```
O(n log n)
```

Two pointer scanning:

```
O(n²)
```

Overall complexity:

```
O(n²)
```

---

## Space Complexity

```
O(1)
```

No additional data structures are required.

---

## Why This Problem Matters

3Sum Closest reinforces the **Two Pointer pattern** and teaches a subtle but important skill: **tracking optimal values while searching**.

This pattern appears frequently in optimization problems and interview questions.
