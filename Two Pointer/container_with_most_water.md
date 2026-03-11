
# Container With Most Water — Understanding the Two Pointer Strategy

Imagine vertical lines drawn on a graph, where each line represents a height. If you pick two lines, they form a container that can hold water. The amount of water depends on the shorter line and the distance between the two lines.

The challenge is to find the pair of lines that can hold the **maximum amount of water**.

---

## The Problem

You are given an array `height` where each element represents the height of a vertical line.

Find two lines that together with the x-axis form a container such that the container holds the **maximum amount of water**.

Return that maximum area.

Example:

```
height = [1,8,6,2,5,4,8,3,7]
```

Output:

```
49
```

Explanation:

The best container is formed by heights `8` and `7` with distance `7`.

Area:

```
7 × 7 = 49
```

---

## Brute Force Approach

We could check every pair of lines:

```
for i in range(n):
    for j in range(i+1,n):
        area = min(height[i],height[j]) * (j-i)
```

Time complexity:

```
O(n²)
```

This becomes very slow for large arrays.

---

## Key Insight

The area is determined by two things:

1. The **distance between lines**
2. The **shorter height**

Formula:

```
area = min(height[left], height[right]) × (right - left)
```

We start with the **widest possible container**.

```
left = 0
right = n - 1
```

Then we gradually move pointers inward.

---

## Why Move the Smaller Height?

Suppose:

```
height[left] < height[right]
```

The container height is limited by `height[left]`.

Moving the right pointer cannot increase the height of the container, so it won’t help.

The only chance to improve the area is to move the **shorter line**.

This is the key idea behind the algorithm.

---

## Algorithm

1. Initialize two pointers

```
left = 0
right = n - 1
```

2. Track the maximum area.

3. While `left < right`:

* Calculate area
* Update maximum
* Move the pointer with the **smaller height**

---

## Python Implementation

```python
def max_area(height):

    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:

        width = right - left
        current_height = min(height[left], height[right])

        area = width * current_height
        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Example
height = [1,8,6,2,5,4,8,3,7]

print(max_area(height))
```

Output:

```
49
```

---

## Time Complexity

Each pointer moves at most `n` times.

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

## Why This Problem Is Important

This problem teaches an important variation of the Two Pointer technique.

Instead of searching for values, the pointers move based on **optimizing a formula**.

This idea appears in many algorithm problems and strengthens your intuition for pointer-based strategies.
