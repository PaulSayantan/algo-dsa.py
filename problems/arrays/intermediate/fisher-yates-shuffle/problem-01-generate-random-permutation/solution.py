"""Generate a uniformly random permutation of [0, n-1].

Classic CLRS "Randomize-In-Place" exercise. Implement the Fisher-Yates
shuffle from scratch; do NOT call random.shuffle.
"""
from typing import List


def random_permutation(n: int) -> List[int]:
    """Return a uniformly random permutation of [0, 1, ..., n - 1].

    Each of the n! orderings must be produced with probability exactly 1/n!.

    Args:
        n: The number of elements; the permutation covers values 0..n-1.

    Returns:
        A list of length n containing each value in [0, n - 1] exactly once,
        in uniformly random order.

    Example:
        >>> perm = random_permutation(3)
        >>> sorted(perm)
        [0, 1, 2]
    """
    # TODO: implement
    # Hint: build arr = [0, 1, ..., n - 1], then for i from n - 1 down to 1
    # pick j = random.randint(0, i) (inclusive) and swap arr[i], arr[j].
    pass


if __name__ == "__main__":
    print(random_permutation(1))   # expected: [0]
    print(sorted(random_permutation(3)))  # expected: [0, 1, 2] (contents, any order)
    print(sorted(random_permutation(5)))  # expected: [0, 1, 2, 3, 4] (contents)
