
# Trapping Rain Water — Using Two Pointers to Measure Water Between Bars

Imagine a landscape made of vertical bars. When it rains, water collects between these bars. The challenge is to calculate how much water can be trapped after rainfall.

This problem looks tricky at first, but once you understand the pattern behind it, the solution becomes elegant.

---

## The Problem

You are given an array `height` where each element represents the height of a bar.

Your task is to compute how much water can be trapped between these bars after raining.

Example:

```id="j0w8j1"
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

Output:

```id="1g17u0"
6
```

Explanation: The bars trap a total of **6 units of water**.

---

## Key Idea

Water trapped at a position depends on two boundaries:

1. The tallest bar on the **left**
2. The tallest bar on the **right**

The water level is limited by the **smaller of these two boundaries**.

Formula:

```id="kj2qki"
water = min(left_max, right_max) - height[i]
```

If the result is positive, that amount of water is trapped at that index.

---

## Two Pointer Strategy

Instead of computing left and right boundaries for every element separately, we can use two pointers.

Initialize:

```id="6w0k1a"
left = 0
right = n - 1
```

Also track:

```id="q8z98o"
left_max
right_max
```

At each step, move the pointer with the **smaller height**, because that side determines the water level.

---

## Algorithm

1. Initialize pointers at both ends.
2. Track the maximum height seen from both sides.
3. Move the pointer with the smaller height.
4. Calculate trapped water at each step.
5. Continue until the pointers meet.

---

## Python Implementation

```python id="mpz70k"
def trap(height):

    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0

    water = 0

    while left < right:

        if height[left] < height[right]:

            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]

            left += 1

        else:

            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]

            right -= 1

    return water


# Example
height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(height))
```

Output:

```id="ig8d6e"
6
```

---

## Time Complexity

Each pointer moves across the array once.

```id="a3kr9x"
O(n)
```

---

## Space Complexity

Only a few variables are used.

```id="5dzq80"
O(1)
```

---

## Why This Problem Is Important

Trapping Rain Water teaches how to combine **two pointers with dynamic boundary tracking**.

The pattern appears in many algorithm problems that involve ranges, heights, or capacity constraints.

Once you understand this idea, you gain stronger intuition for solving complex array problems efficiently.
