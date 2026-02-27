# Aggressive Cows

## Problem Statement

You are given an array of integers `stalls` representing positions of stalls on a number line and an integer `k` representing the number of cows.

Your task is to place the cows in the stalls such that the **minimum distance between any two cows is as large as possible**.

Return the **largest minimum distance**.

---

## Example

Input:

```python
stalls = [1, 2, 4, 8, 9]
k = 3
```

Output:

```python
3
```

Explanation:

We can place cows at positions:

```python
1, 4, 8
```

Minimum distance = 3

This is the maximum possible.

---

## Intuition

This is **not** a direct searching problem.

We are trying to **maximize a minimum value**.

Whenever you see:

> Maximize the minimum
> Minimize the maximum

Think:

```python
Binary Search on Answer
```

Instead of searching an index, we search the **distance**.

Possible distance range:

```python
Minimum distance = 1
Maximum distance = max(stalls) - min(stalls)
```

We binary search this distance.

For each distance, we check:

> Can we place all cows with at least this distance apart?

If yes → try bigger distance
If no → try smaller distance

---

## Key Observation

To check feasibility:

Always place the first cow in the first stall.

Then greedily place the next cow in the next stall that satisfies:

```python
current_position - last_position >= distance
```

If we successfully place all cows → distance is valid.

---

## Algorithm (Binary Search on Answer)

1. Sort the stalls array.

2. Initialize search space:

```python
low = 1
high = stalls[-1] - stalls[0]
```

3. While `low <= high`:

* Find mid distance:

```python
mid = (low + high) // 2
```

* Check if we can place cows with distance = mid.

If possible:

```python
answer = mid
low = mid + 1
```

Try larger distance.

Else:

```python
high = mid - 1
```

Try smaller distance.

4. Return answer.

---

## Feasibility Function

We create a helper function:

```python
can_place_cows(distance)
```

This returns True if cows can be placed with at least that distance.

---

## Dry Run

Stalls:

```python
[1, 2, 4, 8, 9]
k = 3
```

Search space:

```python
low = 1
high = 8
```

Mid = 4

Try placing cows with distance 4:

Placed at:

```python
1 → 8
```

Only 2 cows possible → Not valid

Move left:

```python
high = 3
```

Mid = 2

Place cows:

```python
1 → 4 → 8
```

3 cows placed → Valid

Move right:

```python
low = 3
```

Mid = 3

Place cows:

```python
1 → 4 → 8
```

Valid

Move right:

```python
low = 4
```

Loop ends.

Answer = 3

---

## Python Implementation

```python
def aggressive_cows(stalls, k):
    stalls.sort()

    def can_place(distance):
        count = 1
        last_position = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= distance:
                count += 1
                last_position = stalls[i]

            if count >= k:
                return True

        return False

    low = 1
    high = stalls[-1] - stalls[0]
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if can_place(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer


# Example usage
stalls = [1, 2, 4, 8, 9]
k = 3

print(aggressive_cows(stalls, k))  # Output: 3
```

---

## Time Complexity

Sorting:

```python
O(n log n)
```

Binary search iterations:

```python
O(log(max_distance))
```

Feasibility check each time:

```python
O(n)
```

Overall:

```python
O(n log n + n log D)
```

Where D = range of stall positions.

---

## Space Complexity

```python
O(1)
```

No extra space used.

---

## Key Learning

Very important pattern:

> We are searching the answer, not the index.

This is called:

```python
Binary Search on Answer
```

Once you understand this problem, you can solve:

* Allocate Minimum Pages
* Koko Eating Bananas
* Ship Packages Within D Days
* Minimum Maximum Distance Problems

---

## Interview Tip

Whenever you see:

> Largest minimum
> Smallest maximum

Immediately think:

Binary Search on Answer.

---

## Related Problems

* Allocate Minimum Pages
* Koko Eating Bananas
* Capacity to Ship Packages Within D Days
* Minimum Days to Make Bouquets
