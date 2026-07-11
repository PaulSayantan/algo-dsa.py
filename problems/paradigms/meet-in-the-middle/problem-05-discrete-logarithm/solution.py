"""Discrete Logarithm via Baby-Step Giant-Step.

Find the smallest non-negative x with a^x == b (mod m), where m is prime, or
return -1 if none exists.

Fill in `discrete_log` using Baby-Step Giant-Step, the Meet in the Middle
factoring of the exponent: write x = i*n - j with n = ceil(sqrt(m)), store the
baby steps b * a^j in a hash map, then walk the giant steps (a^n)^i looking for
a collision.
"""

from typing import Dict


def discrete_log(a: int, b: int, m: int) -> int:
    """Return the smallest x >= 0 with a**x % m == b % m, or -1 if none.

    Args:
        a: Base of the exponentiation (0 <= a < m).
        b: Target residue (0 <= b < m).
        m: Prime modulus (2 <= m).

    Returns:
        The smallest non-negative integer x satisfying a**x % m == b % m,
        or -1 if no such x exists.

    Example:
        >>> discrete_log(2, 3, 5)
        3
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    # Expected: 3   (2^3 = 8 == 3 mod 5)
    print(discrete_log(2, 3, 5))
    # Expected: 4   (3^4 = 81 == 13 mod 17)
    print(discrete_log(3, 13, 17))
    # Expected: 16  (5^16 == 3 mod 23)
    print(discrete_log(5, 3, 23))
