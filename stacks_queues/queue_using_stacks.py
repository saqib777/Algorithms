# Algorithm: Two Stacks (push stack + pop stack)
# Amortised Time: O(1) per operation
# Space Complexity: O(n)

class MyQueue:
    """
    Implement a FIFO queue using only two stacks.

    Approach:
    - push_stack: accepts new elements
    - pop_stack:  serves dequeue/peek requests
    - Transfer from push to pop only when pop_stack is empty
      (amortised O(1) per operation)
    """

    def __init__(self):
        self.push_stack = []
        self.pop_stack  = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        self._transfer()
        return self.pop_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack

    def _transfer(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())


# ── test ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # 1
    print(q.pop())    # 1
    print(q.empty())  # False
    print(q.pop())    # 2
    print(q.empty())  # True
