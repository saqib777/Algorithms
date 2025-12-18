The Fibonacci sequence is one of the most common examples used to understand recursion deeply. It clearly shows how a problem can be broken down into overlapping subproblems and also helps explain why naive recursion can be inefficient.

---

Problem Definition

The Fibonacci sequence is defined as:

F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2) for n ≥ 2

Each number is the sum of the two previous numbers.

---

Core Idea

To compute F(n), you need:

* the result of F(n - 1)
* the result of F(n - 2)

Both of these are smaller versions of the same problem. This makes Fibonacci a natural candidate for recursion.

---

Recursive Structure

Every recursive call splits into two more calls:

fib(n)
→ fib(n - 1)
→ fib(n - 2)

This continues until the base cases are reached.

---

Step-by-Step Execution (fib(5))

fib(5)
→ fib(4) + fib(3)
→ (fib(3) + fib(2)) + (fib(2) + fib(1))
→ ((fib(2) + fib(1)) + (fib(1) + fib(0))) + (fib(1) + fib(0))
→ ((1 + 1) + (1 + 0)) + (1 + 0)
→ 5

---

Call Stack Visualization (Text-Based)

fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1)
│   │   │   └── fib(0)
│   │   └── fib(1)
│   └── fib(2)
│       ├── fib(1)
│       └── fib(0)
└── fib(3)
├── fib(2)
│   ├── fib(1)
│   └── fib(0)
└── fib(1)

---

Why Recursive Fibonacci Is Inefficient

Many values are recalculated multiple times.
For example:

* fib(2) is calculated 3 times
* fib(3) is calculated 2 times

This repeated work causes exponential time complexity.

---

Time and Space Complexity

Time Complexity: O(2^n)
Space Complexity: O(n) due to recursion stack

---

Text-Based Flowchart

Start
→ fib(n)
→ If n == 0 → return 0
→ If n == 1 → return 1
→ Else return fib(n - 1) + fib(n - 2)
→ End

---

When to Use Recursive Fibonacci

Primarily for learning and teaching recursion
Not suitable for large values of n

---

Learning Value

Recursive Fibonacci is a perfect example to:

* understand recursion branching
* visualize the call stack
* see the impact of overlapping subproblems

This example naturally leads to optimization techniques like memoization and dynamic programming, which solve the inefficiency problem.
