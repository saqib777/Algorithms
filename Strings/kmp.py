# Algorithm: Knuth-Morris-Pratt (KMP) Pattern Matching
# Time Complexity:  O(n + m) — n = text length, m = pattern length
# Space Complexity: O(m)     — failure function array

def build_failure_function(pattern: str) -> list[int]:
    """
    Build the KMP failure function (also called the partial match table).

    failure[i] = length of the longest proper prefix of pattern[:i+1]
                 that is also a suffix.

    This tells us how far to shift the pattern when a mismatch occurs,
    avoiding redundant comparisons.

    Example:
        pattern = "AABAAB"
        failure = [0, 1, 0, 1, 2, 3]
    """
    m       = len(pattern)
    failure = [0] * m
    j       = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        failure[i] = j

    return failure


def kmp_search(text: str, pattern: str) -> list[int]:
    """
    Find all occurrences of pattern in text using KMP.
    Returns a list of starting indices (0-based).

    Key advantage over naive O(nm) search:
    When a mismatch occurs, the failure function tells us
    exactly how much of the pattern we can skip — never
    re-examining already-matched characters in the text.
    """
    if not pattern or not text:
        return []

    n       = len(text)
    m       = len(pattern)
    failure = build_failure_function(pattern)
    matches = []
    j       = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = failure[j - 1]

    return matches


def count_occurrences(text: str, pattern: str) -> int:
    """Return the count of non-overlapping pattern occurrences in text."""
    return len(kmp_search(text, pattern))


if __name__ == "__main__":
    print(kmp_search("AABAACAADAABAABA", "AABA"))   # [0, 9, 12]
    print(kmp_search("aabxaabyaabz",     "aab"))    # [0, 4, 8]
    print(kmp_search("aaaa",             "aa"))     # [0, 1, 2]
    print(kmp_search("hello",            "world"))  # []

    print(build_failure_function("AABAAB"))         # [0,1,0,1,2,3]
    print(count_occurrences("AABAACAADAABAABA", "AABA"))  # 3
