# Koko Eating Bananas

## Problem Statement

Koko loves to eat bananas.

You are given an array `piles` where each element represents the number of bananas in a pile, and an integer `h` representing the number of hours available.

Koko can decide her eating speed `k` (bananas per hour).

Each hour, she chooses a pile and eats up to `k` bananas from that pile.

If the pile has fewer than `k` bananas, she eats all of them and stops for that hour.

Your task is to find the **minimum integer eating speed `k`** such that Koko can finish all bananas within `h` hours.

---

## Example

Input:

```python
piles = [3, 6, 7, 11]
h = 8
```

Output:

```python
4
```

Explanation:

At speed 4:

Hours needed:

3 → 1 hour
6 → 2 hours
7 → 2 hours
11 → 3 hours

Total = 8 hours (valid)

---

## Intuition

We are asked to:

> Minimize the eating speed

This is another:

```python
Binary Search on Answer
```

We are not searching an index.

We are searching the **minimum speed** that satisfies a condition.

---

## Search Space

Minimum speed:

```python
1
```

Maximum speed:

```python
max(piles)
```

Because if she eats the largest pile in one hour, that is the fastest required.

So:

```python
low = 1
high = max(piles)
```

---

## Feasibility Logic

We check:

> If Koko eats at speed = `mid`, can she finish within `h` hours?

Time required for one pile:

```python
ceil(pile / mid)
```

Total hours = sum of all pile hours.

If total hours ≤ h → valid speed
Else → too slow

---

## Algorithm (Binary Search on Answer)

1. Initialize:

```python
low = 1
high = max(piles)
```

2. While `low <= high`:

Find mid speed:

```python
mid = (low + high) // 2
```

Check feasibility.

If valid:

```python
answer = mid
high = mid - 1
```

Try smaller speed.

Else:

```python
low = mid + 1
```

3. Return answer.

---

## Dry Run

Piles:

```python
[3, 6, 7, 11]
h = 8
```

Search space:

```python
low = 1
high = 11
```

Mid = 6 → possible → try smaller
Mid = 3 → not possible → increase
Mid = 4 → possible → answer
Mid = 3 fails → final answer = 4

---

## Python Implementation

```python
import math

def minEatingSpeed(piles, h):

    def can_finish(speed):
        total_hours = 0

        for pile in piles:
            total_hours += math.ceil(pile / speed)

        return total_hours <= h

    low = 1
    high = max(piles)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        if can_finish(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


# Example usage
piles = [3, 6, 7, 11]
h = 8

print(minEatingSpeed(piles, h))  # Output: 4
```

---

## Time Complexity

Binary search iterations:

```python
O(log(max(piles)))
```

Feasibility check each iteration:

```python
O(n)
```

Overall:

```python
O(n log(max))
```

---

## Space Complexity

```python
O(1)
```

No extra memory used.

---

## Key Learning

Important Binary Search on Answer pattern:

Aggressive Cows → Maximize minimum distance

Allocate Pages → Minimize maximum pages

Koko Eating Bananas → Minimize speed

Same structure, different feasibility condition.

---

## Interview Tip

Whenever you see:

* Minimum speed
* Minimum rate
* Minimum capacity
* Finish within time limit

Think:

Binary Search on Answer.

---

## Related Problems

* Aggressive Cows
* Allocate Minimum Pages
* Capacity to Ship Packages Within D Days
* Minimum Days to Make Bouquets
* Split Array Largest Sum
