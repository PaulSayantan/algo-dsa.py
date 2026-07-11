"""Powerful Array (Codeforces 86D) — empty solution template.

Fill in the body using Mo's algorithm (offline sqrt decomposition on queries).
Do NOT change the function signature.
"""
from typing import List, Tuple


def powerful_array(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """For each query (l, r) return the power of subarray a[l..r].

    Power is defined as sum over distinct values s of (Ks^2 * s), where Ks is the
    number of occurrences of s in the subarray.

    Args:
        a: The static input array of positive integers (0-indexed internally).
        queries: A list of (l, r) pairs, 1-indexed and inclusive
            (1 <= l <= r <= len(a)), matching the problem statement.

    Returns:
        A list of integers, one per query in the ORIGINAL query order, where the
        i-th entry is the power of the requested subarray. Values may exceed
        32 bits.

    Example:
        >>> powerful_array([1, 2, 1], [(1, 2), (1, 3)])
        [3, 6]
    """
    # TODO: implement using Mo's algorithm:
    #   1. Convert 1-indexed (l, r) to 0-indexed window bounds.
    #   2. Choose block size B ~ sqrt(n) and sort queries by (l // B, r).
    #   3. Maintain freq[value] and a running `power`. When adding value v with
    #      current count k: power += (2*k + 1) * v, then freq[v] += 1.
    #      When removing value v with count k: freq[v] -= 1,
    #      power -= (2*(k-1) + 1) * v  (i.e. -(2*new_count + 1) * v).
    #   4. Slide curL/curR to each query and record the answer at its original
    #      position.
    pass


if __name__ == "__main__":
    sample_a = [1, 2, 1]
    sample_queries = [(1, 2), (1, 3)]
    print(powerful_array(sample_a, sample_queries))
    # Expected: [3, 6]
