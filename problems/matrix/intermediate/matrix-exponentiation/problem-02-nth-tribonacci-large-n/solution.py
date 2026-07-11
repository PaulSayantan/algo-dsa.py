"""N-th Tribonacci number for very large n, modulo 1e9+7.

Fill in the body using Matrix Exponentiation on a 3x3 transition matrix.
Do NOT use an O(n) loop — n can be as large as 10**18.
"""

MOD = 10**9 + 7


def tribonacci(n: int) -> int:
    """Return T(n) modulo 10**9 + 7.

    The Tribonacci sequence is T(0)=0, T(1)=1, T(2)=1, and
    T(n)=T(n-1)+T(n-2)+T(n-3) for n >= 3.

    Args:
        n: Index into the Tribonacci sequence, 0 <= n <= 10**18.

    Returns:
        T(n) taken modulo 10**9 + 7.

    Example:
        >>> tribonacci(10)
        149
    """
    # TODO: implement using matrix exponentiation on the 3x3 matrix
    #       [[1, 1, 1], [1, 0, 0], [0, 1, 0]] raised to the appropriate power.
    pass


if __name__ == "__main__":
    print(tribonacci(4))   # expected: 4
    print(tribonacci(10))  # expected: 149
    print(tribonacci(25))  # expected: 1389537
