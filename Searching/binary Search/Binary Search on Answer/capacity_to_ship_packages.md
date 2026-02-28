# Capacity to Ship Packages Within D Days

## Problem Statement

You are given an array `weights` where each element represents the weight of a package placed on a conveyor belt, and an integer `days` representing the number of days to ship all packages.

Packages must be shipped in the given order.

Each day, you load packages onto a ship until the total weight reaches the ship’s capacity.

Your task is to find the **minimum ship capacity** required to ship all packages within `days`.

---

## Example

Input:

```python
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
```

Output:

```python
15
```

Explanation:

One possible shipment:

Day 1 → 1 + 2 + 3 + 4 + 5 = 15
Day 2 → 6 + 7 = 13
Day 3 → 8
Day 4 → 9
Day 5 → 10

Minimum capacity needed = 15

---

## Intuition

We are asked to:

> Minimize the ship capacity

This is a classic:

Binary Search on Answer

We are not searching an index.

We are searching the **minimum capacity** that allows shipment within `days`.

---

## Search Space

Minimum possible capacity:

```python
max(weights)
```

Because the largest package must fit.

Maximum possible capacity:

```python
sum(weights)
```

Ship everything in one day.

So:

```python
low = max(weights)
high = sum(weights)
```

---

## Feasibility Logic

We check:

> If ship capacity = `mid`, can we ship within `days`?

Greedy approach:

* Keep loading packages until capacity exceeds `mid`
* Then move to the next day

If required days ≤ given days → valid
Else → invalid

---

## Algorithm (Binary Search on Answer)

1. Initialize:

```python
low = max(weights)
high = sum(weights)
```

2. While `low <= high`:

Find mid capacity:

```python
mid = (low + high) // 2
```

Check feasibility.

If valid:

```python
answer = mid
high = mid - 1
```

Try smaller capacity.

Else:

```python
low = mid + 1
```

3. Return answer.

---

## Dry Run

Weights:

```python
[1,2,3,4,5,6,7,8,9,10]
days = 5
```

Search space:

```python
low = 10
high = 55
```

Mid = 32 → possible → try smaller
Mid = 21 → possible → try smaller
Mid = 15 → possible → try smaller
Mid = 12 → not possible → increase

Final answer = 15

---

## Python Implementation

```python
def shipWithinDays(weights, days):

    def can_ship(capacity):
        required_days = 1
        current_load = 0

        for weight in weights:
            if current_load + weight > capacity:
                required_days += 1
                current_load = weight
            else:
                current_load += weight

        return required_days <= days

    low = max(weights)
    high = sum(weights)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        if can_ship(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


# Example usage
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(shipWithinDays(weights, days))  # Output: 15
```

---

## Time Complexity

Binary search iterations:

O(log(sum(weights)))

Feasibility check each iteration:

O(n)

Overall:

O(n log(sum))

---

## Space Complexity

O(1)

No extra memory used.

---

## Key Learning

Binary Search on Answer pattern:

Aggressive Cows → maximize minimum distance
Allocate Pages → minimize maximum load
Koko → minimize speed
Ship Packages → minimize capacity

Same structure, different feasibility condition.

---

## Interview Tip

Whenever you see:

* Minimum capacity
* Finish within given days
* Split work into parts
* Load balancing

Think Binary Search on Answer.

---

## Related Problems

* Aggressive Cows
* Allocate Minimum Pages
* Koko Eating Bananas
* Split Array Largest Sum
* Minimum Days to Make Bouquets
