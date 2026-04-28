# Algorithm: Euclidean Algorithm
# Time Complexity:  O(log min(a,b)) — number of steps bounded by Fibonacci
# Space Complexity: O(1) iterative | O(log min(a,b)) recursive

def gcd_recursive(a: int, b: int) -> int:
    """
    Greatest Common Divisor using Euclidean algorithm (recursive).

    Principle: gcd(a, b) = gcd(b, a mod b)
    Base case: gcd(a, 0) = a

    Example: gcd(48, 18)
        gcd(48,18) → gcd(18,12) → gcd(12,6) → gcd(6,0) = 6
    """
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def gcd_iterative(a: int, b: int) -> int:
    """Iterative version — no recursion overhead."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Least Common Multiple.
    Uses the relationship: lcm(a,b) = |a*b| / gcd(a,b)
    Divide first to avoid integer overflow.
    """
    return abs(a * b) // gcd_iterative(a, b)


def gcd_multiple(nums: list[int]) -> int:
    """GCD of a list of numbers using reduce."""
    from functools import reduce
    return reduce(gcd_iterative, nums)


def lcm_multiple(nums: list[int]) -> int:
    """LCM of a list of numbers using reduce."""
    from functools import reduce
    return reduce(lcm, nums)


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) such that: a*x + b*y = gcd(a,b)
    Used in modular inverse computation.
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1  = extended_gcd(b, a % b)
    x          = y1
    y          = x1 - (a // b) * y1
    return g, x, y


if __name__ == "__main__":
    print(gcd_recursive(48, 18))       # 6
    print(gcd_iterative(48, 18))       # 6
    print(lcm(4, 6))                   # 12
    print(lcm(12, 18))                 # 36

    print(gcd_multiple([12, 18, 24]))  # 6
    print(lcm_multiple([4, 6, 10]))    # 60

    g, x, y = extended_gcd(35, 15)
    print(g, x, y)                     # 5, 1, -2
    print(35*x + 15*y == g)            # True
