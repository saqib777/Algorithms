# Algorithm: Sliding Window (Variable Size)
# Time Complexity:  O(n) — each character added and removed at most once
# Space Complexity: O(k) — k = size of character set

from collections import defaultdict


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find the length of the longest substring with at most k distinct characters.

    Sliding window: expand right pointer, shrink left pointer
    when the window has more than k distinct characters.
    """
    if k == 0 or not s:
        return 0

    freq  = defaultdict(int)
    left  = 0
    best  = 0

    for right in range(len(s)):
        freq[s[right]] += 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        best = max(best, right - left + 1)

    return best


def min_window_substring(s: str, t: str) -> str:
    """
    Find the minimum window in s that contains all characters of t.
    Returns empty string if no such window exists.

    Two-pointer sliding window with frequency maps.
    Time: O(n + m) where n = len(s), m = len(t)
    """
    if not s or not t:
        return ""

    need    = defaultdict(int)
    for ch in t:
        need[ch] += 1

    have      = defaultdict(int)
    formed    = 0
    required  = len(need)
    left      = 0
    best      = float('inf')
    best_left = 0

    for right in range(len(s)):
        ch = s[right]
        have[ch] += 1
        if ch in need and have[ch] == need[ch]:
            formed += 1

        while formed == required:
            if right - left + 1 < best:
                best      = right - left + 1
                best_left = left
            lch = s[left]
            have[lch] -= 1
            if lch in need and have[lch] < need[lch]:
                formed -= 1
            left += 1

    return s[best_left:best_left + best] if best != float('inf') else ""


def find_all_anagrams(s: str, p: str) -> list[int]:
    """
    Find all starting indices of anagrams of p in s.
    Fixed-size sliding window of length len(p).
    Time: O(n)
    """
    if len(p) > len(s):
        return []

    p_count = defaultdict(int)
    w_count = defaultdict(int)

    for ch in p:
        p_count[ch] += 1

    result = []
    k      = len(p)

    for i in range(len(s)):
        w_count[s[i]] += 1
        if i >= k:
            old = s[i - k]
            w_count[old] -= 1
            if w_count[old] == 0:
                del w_count[old]
        if w_count == p_count:
            result.append(i - k + 1)

    return result


if __name__ == "__main__":
    print(longest_substring_k_distinct("eceba", 2))    # 3 → "ece"
    print(longest_substring_k_distinct("aa", 1))       # 2
    print(min_window_substring("ADOBECODEBANC", "ABC")) # "BANC"
    print(min_window_substring("a", "a"))               # "a"
    print(find_all_anagrams("cbaebabacd", "abc"))       # [0, 6]
    print(find_all_anagrams("abab", "ab"))              # [0, 1, 2]
