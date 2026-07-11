"""Sample k distinct elements uniformly without replacement.

Generalization of shuffling (k == n is a full shuffle). Implement a
partial Fisher-Yates; do NOT call random.sample.
"""
from typing import List


def sample_k(nums: List[int], k: int) -> List[int]:
    """Return k elements chosen uniformly at random without replacement.

    Every C(n, k) subset must be equally likely, and no element repeats.

    Args:
        nums: A list of n distinct integers.
        k: Number of elements to sample, with 0 <= k <= len(nums).

    Returns:
        A list of k distinct elements drawn from nums.

    Example:
        >>> out = sample_k([10, 20, 30, 40], 2)
        >>> len(out) == 2 and len(set(out)) == 2
        True
    """
    # TODO: implement
    # Hint: copy nums, then for i in range(k): pick j = random.randint(i, n-1)
    # and swap arr[i], arr[j]. Return arr[:k].
    pass


if __name__ == "__main__":
    print(sorted(sample_k([10, 20, 30, 40], 2)))  # expected: 2 distinct values from the set
    print(sorted(sample_k([5, 6, 7], 3)))          # expected: [5, 6, 7] (full shuffle contents)
    print(sample_k([42], 0))                        # expected: []
