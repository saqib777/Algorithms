# Algorithm: Binary Exponentiation (Exponentiation by Squaring)
# Time Complexity:  O(log n) — halves the exponent each step
# Space Complexity: O(log n) recursive | O(1) iterative

def power_recursive(base: float, exp: int) -> float:
    """
    Compute base^exp using recursive binary exponentiation.

    Key insight: if exp is even:   base^exp = (base^2)^(exp/2)
                 if exp is odd:    base^exp = base * base^(exp-1)

    This halves the problem each time → O(log n) multiplications
    instead of O(n) for naive repeated multiplication.

    Handles negative exponents via 1 / power(base, -exp).
    """
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power_recursive(base, -exp)
    if exp % 2 == 0:
        half = power_recursive(base, exp // 2)
        return half * half
    return base * power_recursive(base, exp - 1)


def power_iterative(base: float, exp: int) -> float:
    """
    Iterative binary exponentiation.
    Process each bit of the exponent from right to left.
    If bit is 1, multiply result by current power of base.
    """
    if exp < 0:
        base = 1 / base
        exp  = -exp

    result = 1.0

    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base  *= base
        exp   //= 2

    return result


def power_mod(base: int, exp: int, mod: int) -> int:
    """
    Modular exponentiation: (base^exp) % mod
    Critical in cryptography (RSA), competitive programming.
    Uses Python's built-in 3-argument pow for maximum efficiency.
    """
    return pow(base, exp, mod)


def power_mod_manual(base: int, exp: int, mod: int) -> int:
    """Manual implementation of modular exponentiation."""
    result = 1
    base   = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp  //= 2
        base   = (base * base) % mod

    return result


if __name__ == "__main__":
    for fn in [power_recursive, power_iterative]:
        print(fn(2, 10))     # 1024.0
        print(fn(2, -2))     # 0.25
        print(fn(3, 0))      # 1.0
        print(fn(1.5, 4))    # 5.0625
        print("---")

    print(power_mod(2, 10, 1000))         # 24
    print(power_mod_manual(2, 10, 1000))  # 24
    print(power_mod(3, 200, 13))          # fast even for huge exponents
