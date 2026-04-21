# Algorithm: DP + Binary Search (Patience Sorting)
# Time Complexity:  O(n log n) — binary search on tails array
# Space Complexity: O(n)       — tails array

import bisect


def lis_dp(nums: list[int]) -> int:
    """
    O(n^2) DP approach — intuitive.
    dp[i] = length of longest increasing subsequence ending at index i.
    """
    if not nums:
        return 0
    n  = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_binary_search(nums: list[int]) -> int:
    """
    O(n log n) approach using patience sorting / binary search.
    Maintains a 'tails' array where tails[i] is the smallest tail
    element of all increasing subsequences of length i+1.

    This does NOT reconstruct the actual subsequence —
    only returns the length.
    """
    if not nums:
        return 0

    tails = []

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


def lis_with_sequence(nums: list[int]) -> tuple[int, list[int]]:
    """
    O(n^2) DP that also reconstructs the actual subsequence.
    Returns (length, one valid subsequence).
    """
    if not nums:
        return 0, []
    n      = len(nums)
    dp     = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i]     = dp[j] + 1
                parent[i] = j

    max_len = max(dp)
    idx     = dp.index(max_len)
    seq     = []
    while idx != -1:
        seq.append(nums[idx])
        idx = parent[idx]

    return max_len, seq[::-1]


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lis_dp(nums))             # 4
    print(lis_binary_search(nums))  # 4

    length, seq = lis_with_sequence(nums)
    print(length, seq)              # 4  [2, 3, 7, 18] or similar
