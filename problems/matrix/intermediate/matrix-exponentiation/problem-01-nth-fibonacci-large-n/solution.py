"""N-th Fibonacci number for very large n, modulo 1e9+7.

Fill in the body using Matrix Exponentiation. Do NOT use an O(n) loop —
n can be as large as 10**18.
"""

MOD = 10**9 + 7


def fibonacci(n: int) -> int:
    """Return F(n) modulo 10**9 + 7.

    The Fibonacci sequence is F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).

    Args:
        n: Index into the Fibonacci sequence, 0 <= n <= 10**18.

    Returns:
        F(n) taken modulo 10**9 + 7.

    Example:
        >>> fibonacci(10)
        55
    """
    # TODO: implement using matrix exponentiation on the 2x2 matrix
    #       [[1, 1], [1, 0]] raised to the n-th power.
    pass


if __name__ == "__main__":
    print(fibonacci(2))   # expected: 1
    print(fibonacci(10))  # expected: 55
    print(fibonacci(50))  # expected: 586268941
