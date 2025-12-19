Recursion Basics Explanation

Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller versions of the same problem. Instead of solving everything at once, recursion focuses on solving one small piece and trusting that the remaining pieces will be handled by future recursive calls.

---

Core Idea

Every recursive solution is built on two essential parts:

1. Base Case - the condition where recursion stops
2. Recursive Case - the part where the function calls itself

Without a base case, recursion will run forever and cause a stack overflow.

---

How Recursion Works Internally

When a recursive function is called, the system stores its state (parameters, local variables, return address) on the call stack. Each recursive call adds a new stack frame. When a base case is reached, the function starts returning values, and the stack frames are removed one by one.

This process is called stack unwinding.

---

Simple Example (Conceptual)

Factorial of n:

factorial(n) = n × factorial(n-1)
Base case:
factorial(0) = 1

If n = 4:
4 × factorial(3)
3 × factorial(2)
2 × factorial(1)
1 × factorial(0)

Now the base case is reached, and values return upward.

---

Text-Based Flow of Recursion

Start factorial(4)
→ factorial(3)
→ factorial(2)
→ factorial(1)
→ factorial(0)
→ return 1
→ return 1 × 1
→ return 2 × 1
→ return 3 × 2
→ return 4 × 6

---

Common Characteristics of Recursive Problems

* Problem can be divided into smaller subproblems of the same type
* There is a clear stopping condition
* The same logic applies at every level

---

Time and Space Considerations

Time complexity depends on how many times the function is called.
Space complexity depends on recursion depth because of the call stack.

Even if no extra memory is used, recursion still consumes stack space.

---

When to Use Recursion

* Tree and graph traversal
* Divide and conquer algorithms
* Backtracking problems
* Problems with natural self-similar structure

---

When Not to Use Recursion

* Very deep recursion without tail-call optimization
* Simple loops where iteration is clearer and safer

---

Learning Value

Understanding recursion is critical for mastering backtracking, trees, graphs, and dynamic programming. If recursion feels confusing at first, that is normal. It becomes clear once you learn to trust the base case and visualize the call stack.

```
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Fibonacci of 6:", fibonacci(6))
```
