# Algorithm: Single Queue with rotation on push
# Time Complexity:  push O(n) | pop O(1) | top O(1)
# Space Complexity: O(n)

from collections import deque


class MyStack:
    """
    Implement a LIFO stack using a single queue.

    Approach:
    - On every push, rotate the queue so the newest element
      is always at the front (ready to be popped).
    - pop and top are then O(1).
    """

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# ── test ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    print(s.top())    # 2
    print(s.pop())    # 2
    print(s.empty())  # False
    print(s.pop())    # 1
    print(s.empty())  # True
