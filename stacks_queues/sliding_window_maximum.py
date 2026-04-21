# Algorithm: Monotonic Deque (Decreasing)
# Time Complexity:  O(n) — each element added and removed from deque at most once
# Space Complexity: O(k) — deque holds at most k indices at a time

from collections import deque


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    """
    Given an array and a sliding window of size k,
    return the maximum value in each window position.

    Brute force is O(n*k). This deque approach is O(n).

    Approach: maintain a decreasing deque of indices.
    The front of the deque is always the index of the
    current window's maximum element.

    Example:
        nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3, 3, 5, 5, 6, 7]
    """
    if not nums or k == 0:
        return []

    dq     = deque()   # stores indices, not values
    result = []

    for i in range(len(nums)):
        # Remove indices outside the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices of smaller elements from the back
        # They can never be the window maximum
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Start adding results once the first window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    print(sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
    print(sliding_window_maximum([1], 1))                    # [1]
    print(sliding_window_maximum([1,-1], 1))                 # [1,-1]
    print(sliding_window_maximum([9,11], 2))                 # [11]
