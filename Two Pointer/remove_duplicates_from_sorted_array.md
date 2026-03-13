# Remove Duplicates from Sorted Array — In-Place Two Pointer Technique

When working with sorted arrays, duplicates often appear together. A common task is to remove these duplicates while keeping only unique elements.

The challenge is to do this **without using extra space**.

This is where the **Two Pointer technique** becomes extremely useful.

---

## The Problem

You are given a **sorted array** `nums`.

Remove the duplicates **in-place** such that each element appears only once.

Return the number of unique elements.

Example:

```
nums = [1,1,2]
```

Output:

```
2
```

Modified array:

```
[1,2,_]
```

Another example:

```
nums = [0,0,1,1,1,2,2,3,3,4]
```

Output:

```
5
```

Modified array:

```
[0,1,2,3,4]
```

---

## Key Idea

Because the array is **sorted**, duplicates always appear next to each other.

We can use two pointers:

Pointer 1 → tracks the **position of unique elements**
Pointer 2 → scans the array

Whenever we encounter a new unique value, we move it forward.

---

## Visualization

Example:

```
[0,0,1,1,1,2,2,3,3,4]
```

Pointer movement:

```
slow → unique elements
fast → scanning pointer
```

Whenever `nums[fast]` differs from the previous element, we place it at the next unique position.

---

## Algorithm

1. If the array is empty, return 0.
2. Initialize a pointer for unique elements.
3. Traverse the array using another pointer.
4. When a new value is found, place it in the next unique position.
5. Return the count of unique elements.

---

## Python Implementation

```python
def remove_duplicates(nums):

    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):

        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


# Example
nums = [0,0,1,1,1,2,2,3,3,4]

k = remove_duplicates(nums)

print(k)
print(nums[:k])
```

Output:

```
5
[0,1,2,3,4]
```

---

## Time Complexity

We traverse the array once.

```
O(n)
```

---

## Space Complexity

The array is modified in-place.

```
O(1)
```

---

## Why This Problem Is Important

This problem teaches an important pattern:

**Using one pointer to scan and another to maintain structure.**

This idea appears in many array manipulation problems such as:

* Remove Element
* Move Zeroes
* Merge Sorted Arrays
* Partitioning problems

