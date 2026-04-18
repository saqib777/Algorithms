# Algorithm: Monotonic Stack
# Time Complexity:  O(n) — each element pushed and popped at most once
# Space Complexity: O(n) — stack and result map

def next_greater_element(nums: list[int]) -> list[int]:
    """
    For each element in nums, find the next greater element
    to its right. Return -1 if no greater element exists.

    Example:
        Input:  [2, 1, 2, 4, 3]
        Output: [4, 2, 4, -1, -1]

    Approach: monotonic decreasing stack.
    - Iterate left to right.
    - While stack top is less than current number,
      the current number is the answer for the stack top.
    """
    n      = len(nums)
    result = [-1] * n
    stack  = []  # stores indices

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx         = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


def next_greater_element_circular(nums: list[int]) -> list[int]:
    """
    Variant: circular array — wrap around when searching.
    Traverse the array twice using modulo.
    """
    n      = len(nums)
    result = [-1] * n
    stack  = []

    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            idx         = stack.pop()
            result[idx] = nums[i % n]
        if i < n:
            stack.append(i)

    return result


# ── test ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(next_greater_element([2, 1, 2, 4, 3]))     # [4, 2, 4, -1, -1]
    print(next_greater_element([1, 3, 2, 4]))         # [3, 4, 4, -1]
    print(next_greater_element_circular([1, 2, 1]))   # [2, -1, 2]
