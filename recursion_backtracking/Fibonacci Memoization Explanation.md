Memoization is an optimization technique used with recursion to avoid repeated calculations. It stores the results of expensive function calls and reuses them when the same inputs occur again.

---

Why Memoization Is Needed

In naive recursive Fibonacci, the same values are recomputed many times. For example, fib(3) and fib(2) are recalculated repeatedly. This leads to exponential time complexity.

Memoization fixes this by remembering results once they are computed.

---

Core Idea

Use a data structure (usually a dictionary or array) to store previously computed results.

When the function is called:

* If the result is already stored, return it immediately.
* Otherwise, compute it, store it, and then return it.

---

How Memoization Changes the Call Tree

Without memoization:

* The recursion tree branches heavily.

With memoization:

* Each Fibonacci number is computed exactly once.
* Recursive calls collapse into a straight line of dependencies.

---

Step-by-Step Example (fib(5))

Call fib(5)
→ fib(4) + fib(3)
→ fib(3) + fib(2) + fib(3)

With memoization:

* fib(3) is computed once and stored
* Subsequent calls reuse the stored value

---

Text-Based Flowchart

Start
→ fib(n)
→ If n in memo → return memo[n]
→ If n == 0 or n == 1 → return n
→ memo[n] = fib(n-1) + fib(n-2)
→ return memo[n]
→ End

---

Algorithm Structure (Step Form)

1. Initialize memo storage
2. Define recursive function
3. Check memo before computation
4. Store computed result
5. Return result

---

Time and Space Complexity

Time Complexity: O(n)
Space Complexity: O(n) for memo storage and recursion stack

---

Properties

Uses recursion with optimization
Avoids redundant computation
Transforms exponential algorithms into linear ones

---

When to Use

When recursion has overlapping subproblems
When dynamic programming is applicable
When readability of recursion is desired with performance

---

Learning Value

Memoization is the bridge between recursion and dynamic programming. Mastering this concept prepares you for advanced DP problems and performance optimization techniques.

```
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    n = 10
    print("Fibonacci of", n, "is", fibonacci(n))
```
