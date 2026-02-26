# Search Insert Position

## Problem Statement

Given a **sorted array of distinct integers** and a **target value**, return the index if the target is found.

If the target is not found, return the index where it would be inserted in order.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Example

Input:

```
nums = [1, 3, 5, 6]
target = 5
```

Output:

```
2
```

Input:

```
nums = [1, 3, 5, 6]
target = 2
```

Output:

```
1
```

Input:

```
nums = [1, 3, 5, 6]
target = 7
```

Output:

```
4
```

---

## Intuition

This problem is a direct application of **Binary Search**.

There are only two possibilities:

1. Target exists → return its index.
2. Target does not exist → return the position where it should be inserted.

The key observation:

When binary search finishes, the `low` pointer will always be pointing to the correct insertion position.

So even if we don't find the target, we simply return `low`.

---

## Algorithm (Binary Search)

1. Initialize:

```
low = 0
high = n - 1
```

2. While `low <= high`:

* Find middle index:

```
mid = low + (high - low) / 2
```

* If target equals middle → return mid
* If target is greater → search right half

```
low = mid + 1
```

* If target is smaller → search left half

```
high = mid - 1
```

3. If loop ends, return `low`.

`low` represents the correct insertion position.

---

## Dry Run

Array:

```
[1, 3, 5, 6]
target = 2
```

Step 1:

```
low = 0, high = 3
mid = 1 → value = 3
```

Target < 3 → move left

```
high = mid - 1 = 0
```

Step 2:

```
low = 0, high = 0
mid = 0 → value = 1
```

Target > 1 → move right

```
low = mid + 1 = 1
```

Now:

```
low = 1, high = 0 → loop ends
```

Return:

```
low = 1
```

Correct insertion index.

---

## Java Implementation

```java
public class SearchInsertPosition {

    public static int searchInsert(int[] nums, int target) {

        int low = 0;
        int high = nums.length - 1;

        while (low <= high) {

            int mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return low;
    }

    public static void main(String[] args) {

        int[] nums = {1, 3, 5, 6};

        System.out.println(searchInsert(nums, 5)); // 2
        System.out.println(searchInsert(nums, 2)); // 1
        System.out.println(searchInsert(nums, 7)); // 4
    }
}
```

---

## Time Complexity

Binary search reduces search space by half every step.

```
Time Complexity: O(log n)
```

---

## Space Complexity

No extra memory is used.

```
Space Complexity: O(1)
```

---

## Key Learning

Very important concept:

> When binary search ends, `low` always points to the correct insertion index.

This idea is heavily used in:

* Lower Bound
* Upper Bound
* First and Last Occurrence
* Binary Search on Answer problems

---

## Related Problems

* Lower Bound
* Upper Bound
* First and Last Position of Element in Sorted Array
* Find Minimum in Rotated Sorted Array

---

## Interview Tip

If you forget the logic during interview, remember:

> Just perform normal binary search.
> If not found, return `low`.

That alone solves the problem.
