# Algorithm: Z-Algorithm for Pattern Matching
# Time Complexity:  O(n + m) — n = text, m = pattern
# Space Complexity: O(n + m) — Z array of combined length

def build_z_array(s: str) -> list[int]:
    """
    Build the Z array for string s.

    Z[i] = length of the longest substring starting at s[i]
           that is also a prefix of s.
    Z[0] is undefined (conventionally 0 or len(s)).

    Example:
        s    = "aabxaa"
        Z    = [0, 1, 0, 0, 2, 1]
               s[1]="a"  matches prefix "a"  → Z[1]=1
               s[4]="aa" matches prefix "aa" → Z[4]=2

    Used in: pattern matching, string compression,
             counting distinct substrings.
    """
    n      = len(s)
    z      = [0] * n
    left   = right = 0

    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] > right:
            left  = i
            right = i + z[i]

    return z


def z_search(text: str, pattern: str) -> list[int]:
    """
    Find all occurrences of pattern in text using Z algorithm.
    Returns list of starting indices (0-based).

    Approach: concatenate pattern + '$' + text.
    Any position in the Z array equal to len(pattern)
    marks an occurrence in the text.
    """
    if not pattern or not text:
        return []

    combined = pattern + '$' + text
    z        = build_z_array(combined)
    m        = len(pattern)
    matches  = []

    for i in range(m + 1, len(combined)):
        if z[i] == m:
            matches.append(i - m - 1)

    return matches


def shortest_palindrome(s: str) -> str:
    """
    Find the shortest palindrome by adding characters to the front.

    Uses Z array to find the longest palindromic prefix,
    then prepends the remaining reversed suffix.

    Example: "abcd" → "dcbabcd"
    """
    rev      = s[::-1]
    combined = s + '#' + rev
    z        = build_z_array(combined)
    n        = len(s)

    # Find longest prefix of s that is also a palindrome
    for i in range(len(combined) - 1, n, -1):
        if z[i] == len(combined) - i:
            suffix_start = len(combined) - i
            return rev[:suffix_start] + s

    return rev + s


if __name__ == "__main__":
    print(build_z_array("aabxaa"))          # [0,1,0,0,2,1]
    print(build_z_array("aaaa"))            # [0,3,2,1]
    print(build_z_array("abcabc"))          # [0,0,0,3,0,0] -- wait
    # Correct: [0,0,0,3,0,0] means s[3:]="abc" matches prefix "abc" of len 3

    print(z_search("AABAACAADAABAABA","AABA"))   # [0, 9, 12]
    print(z_search("aabxaabyaabz","aab"))         # [0, 4, 8]
    print(z_search("hello","world"))              # []

    print(shortest_palindrome("abcd"))    # "dcbabcd"
    print(shortest_palindrome("aacecaaa")) # "aaacecaaa"
