# Algorithm: Modular Arithmetic — core number theory for DSA
# All operations O(log n) or better

def mod_add(a: int, b: int, mod: int) -> int:
    """(a + b) % mod — safe for large numbers."""
    return (a % mod + b % mod) % mod


def mod_multiply(a: int, b: int, mod: int) -> int:
    """(a * b) % mod — prevents overflow in other languages."""
    return (a % mod * (b % mod)) % mod


def mod_inverse(a: int, mod: int) -> int:
    """
    Modular multiplicative inverse of a modulo mod.
    Returns x such that (a * x) % mod == 1.

    Requirements: mod must be prime (Fermat's little theorem).
    Uses fast exponentiation: a^(mod-2) % mod

    Application: modular division → (a / b) % mod = (a * b^-1) % mod
    """
    return pow(a, mod - 2, mod)


def mod_divide(a: int, b: int, mod: int) -> int:
    """
    Modular division: (a / b) % mod
    Only valid when mod is prime and gcd(b, mod) == 1.
    """
    return (a % mod * mod_inverse(b, mod)) % mod


def chinese_remainder_theorem(remainders: list[int], moduli: list[int]) -> int:
    """
    Chinese Remainder Theorem (CRT).
    Find x such that:
        x ≡ r[0] (mod m[0])
        x ≡ r[1] (mod m[1])
        ...
    All moduli must be pairwise coprime.
    """
    from math import prod
    M = prod(moduli)
    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        x += r * Mi * pow(Mi, -1, m)
    return x % M


def count_trailing_zeros_factorial(n: int) -> int:
    """
    Count trailing zeros in n!
    Each zero comes from a factor of 10 = 2 * 5.
    Factors of 2 are always more than 5, so count factors of 5.
    """
    count = 0
    power_of_5 = 5
    while power_of_5 <= n:
        count      += n // power_of_5
        power_of_5 *= 5
    return count


def nCr_mod(n: int, r: int, mod: int) -> int:
    """
    Compute C(n,r) % mod efficiently using factorials
    and modular inverse. mod must be prime.
    Time: O(n), Space: O(n)
    """
    if r > n:
        return 0
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % mod
    numerator   = fact[n]
    denominator = fact[r] * fact[n-r] % mod
    return numerator * pow(denominator, mod-2, mod) % mod


if __name__ == "__main__":
    MOD = 10**9 + 7

    print(mod_add(10**9, 10**9, MOD))         # safe addition
    print(mod_multiply(10**9, 10**9, MOD))    # safe multiplication
    print(mod_inverse(3, MOD))                # x where 3x ≡ 1 (mod MOD)
    print(mod_divide(10, 2, MOD))             # 5

    print(chinese_remainder_theorem([2,3,2],[3,5,7]))  # 23

    print(count_trailing_zeros_factorial(25))  # 6
    print(count_trailing_zeros_factorial(100)) # 24

    print(nCr_mod(10, 3, MOD))    # 120
    print(nCr_mod(20, 10, MOD))   # 184756
