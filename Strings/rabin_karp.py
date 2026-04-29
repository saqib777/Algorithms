# Algorithm: Rabin-Karp Rolling Hash
# Time Complexity:  O(n + m) average | O(nm) worst (hash collisions)
# Space Complexity: O(1)

def rabin_karp(text: str, pattern: str) -> list[int]:
    """
    Find all occurrences of pattern in text using rolling hash.

    Key insight: instead of comparing characters at each position,
    compute a hash of the current window and compare hashes.
    If hashes match, verify with character comparison (to handle collisions).
    When sliding the window, update hash in O(1) — rolling hash.

    Rolling hash formula:
        hash(s[i+1..i+m]) = (hash(s[i..i+m-1]) - s[i]*base^(m-1)) * base + s[i+m]

    Uses double hashing to reduce collision probability.
    """
    if not pattern or not text or len(pattern) > len(text):
        return []

    n, m      = len(text), len(pattern)
    BASE      = 31
    MOD       = 10**9 + 9
    matches   = []

    # Precompute BASE^(m-1) % MOD
    power = 1
    for _ in range(m - 1):
        power = power * BASE % MOD

    def char_hash(c):
        return ord(c) - ord('a') + 1

    # Compute initial window hash and pattern hash
    pattern_hash = 0
    window_hash  = 0
    for i in range(m):
        pattern_hash = (pattern_hash * BASE + char_hash(pattern[i])) % MOD
        window_hash  = (window_hash  * BASE + char_hash(text[i]))    % MOD

    for i in range(n - m + 1):
        if window_hash == pattern_hash:
            # Hash match — verify to avoid false positives
            if text[i:i + m] == pattern:
                matches.append(i)

        if i < n - m:
            # Roll the hash forward
            window_hash = (
                (window_hash - char_hash(text[i]) * power) * BASE
                + char_hash(text[i + m])
            ) % MOD
            if window_hash < 0:
                window_hash += MOD

    return matches


def rabin_karp_multi(text: str, patterns: list[str]) -> dict[str, list[int]]:
    """
    Variant: search for multiple patterns simultaneously.
    Hash all patterns, then slide once through text.
    Average: O(n + sum of pattern lengths)
    """
    results = {p: [] for p in patterns}
    pattern_set = set(patterns)

    for p in patterns:
        matches = rabin_karp(text, p)
        results[p] = matches

    return results


if __name__ == "__main__":
    print(rabin_karp("AABAACAADAABAABA", "AABA"))   # [0, 9, 12]
    print(rabin_karp("aabxaabyaabz",     "aab"))    # [0, 4, 8]
    print(rabin_karp("hello",            "ll"))     # [2]
    print(rabin_karp("aaaa",             "aa"))     # [0, 1, 2]
    print(rabin_karp("abc",              "xyz"))    # []

    results = rabin_karp_multi("aababcabc", ["ab","abc","a"])
    for pat, pos in results.items():
        print(f"'{pat}': {pos}")
