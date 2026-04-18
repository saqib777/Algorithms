# Algorithm: Two Stacks (main + auxiliary min tracker)
# Time Complexity:  O(1) for all operations
# Space Complexity: O(n) — two stacks of size n

class MinStack:
    """
    Stack that supports push, pop, top, and retrieving
    the minimum element — all in O(1) time.

    Approach: maintain a second stack that tracks the
    current minimum at every state of the main stack.
    """

    def __init__(self):
        self.stack     = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


# ── test ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.get_min())  # -3
    ms.pop()
    print(ms.top())      # 0
    print(ms.get_min())  # -2
