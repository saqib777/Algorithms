
# Floor and Ceil in Sorted Array

## Problem Statement

Given a **sorted array** `nums` and a target value `target`, find:

* **Floor** → Largest element ≤ target
* **Ceil** → Smallest element ≥ target

Return the result as:

```python
[floor_value, ceil_value]
```

If floor or ceil does not exist, return `-1` in its place.

You must solve it in **O(log n)** time.

---

## Example

Input:

```python
nums = [1, 2, 4, 6, 10]
target = 5
```

Output:

```python
[4, 6]
```

---

Input:

```python
nums = [1, 2, 4, 6, 10]
target = 0
```

Output:

```python
[-1, 1]
```

---

Input:

```python
nums = [1, 2, 4, 6, 10]
target = 12
```

Output:

```python
[10, -1]
```

---

## Intuition

Since the array is sorted:

* If `nums[mid] <= target`, it can be a potential **floor**
* If `nums[mid] >= target`, it can be a potential **ceil**

We use binary search and update candidates as we go.

This is another form of:

Boundary Binary Search

---

## Algorithm

Initialize:

```python
low = 0
high = len(nums) - 1
floor_value = -1
ceil_value = -1
```

While `low <= high`:

1. Compute mid
2. If `nums[mid] == target`
   → Floor and Ceil both equal target
3. If `nums[mid] < target`
   → Update floor = nums[mid]
   → Move right
4. If `nums[mid] > target`
   → Update ceil = nums[mid]
   → Move left

Return `[floor_value, ceil_value]`

---

## Dry Run

Array:

```python
[1, 2, 4, 6, 10]
target = 5
```

Step 1:
mid = 4
4 < 5 → floor = 4 → move right

Step 2:
mid = 6
6 > 5 → ceil = 6 → move left

Loop ends.

Result:

```python
[4, 6]
```

---

## Python Implementation

```python
def floor_and_ceil(nums, target):
    low = 0
    high = len(nums) - 1

    floor_value = -1
    ceil_value = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return [nums[mid], nums[mid]]

        elif nums[mid] < target:
            floor_value = nums[mid]
            low = mid + 1

        else:
            ceil_value = nums[mid]
            high = mid - 1

    return [floor_value, ceil_value]


# Example usage
nums = [1, 2, 4, 6, 10]

print(floor_and_ceil(nums, 5))   # [4, 6]
print(floor_and_ceil(nums, 0))   # [-1, 1]
print(floor_and_ceil(nums, 12))  # [10, -1]
```

---

## Time Complexity

Binary search:

O(log n)

---

## Space Complexity

O(1)

No extra memory used.

---

## Key Learning

Important boundaries:

* Floor exists only if there is an element ≤ target
* Ceil exists only if there is an element ≥ target

This problem reinforces:

* Boundary updates
* Candidate tracking during binary search
* Edge case handling

---

## Interview Tip

If confused:

Think of floor as:

“Last element that does not cross target.”

Think of ceil as:

“First element that crosses target.”

---

## Related Problems

* Lower Bound and Upper Bound
* First and Last Occurrence
* Count Occurrences
* Search Insert Position
