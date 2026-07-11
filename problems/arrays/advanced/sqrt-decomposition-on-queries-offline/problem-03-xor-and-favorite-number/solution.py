"""XOR and Favorite Number (Codeforces 617E) — empty solution template.

Fill in the body using Mo's algorithm (offline sqrt decomposition on queries)
after reformulating subarray XOR via prefix XOR values.
Do NOT change the function signature.
"""
from typing import List, Tuple


def xor_favorite_number(
    a: List[int], k: int, queries: List[Tuple[int, int]]
) -> List[int]:
    """For each query (l, r) count subarrays of a[l..r] whose XOR equals k.

    A subarray a[i..j] (l <= i <= j <= r) counts when
    a[i] XOR ... XOR a[j] == k. Using prefix XOR values pre[t], this is the
    number of prefix-index pairs (x, y), l-1 <= x < y <= r, with
    pre[x] XOR pre[y] == k.

    Args:
        a: The static input array of non-negative integers (0-indexed internally).
        k: The favorite number to match against subarray XORs.
        queries: A list of (l, r) pairs, 1-indexed and inclusive
            (1 <= l <= r <= len(a)), matching the problem statement.

    Returns:
        A list of integers, one per query in the ORIGINAL query order; the i-th
        entry is the count of qualifying subarrays. Values may exceed 32 bits.

    Example:
        >>> xor_favorite_number([1, 2, 1, 1, 0, 3], 3, [(1, 6), (3, 5)])
        [7, 0]
    """
    # TODO: implement using Mo's algorithm:
    #   1. Build prefix XOR array pre[0..n] with pre[0] = 0.
    #   2. Map query (l, r) to the prefix-index window [l-1, r] (inclusive).
    #   3. Choose block size B ~ sqrt(n+1); sort windows by (left // B, right).
    #   4. Maintain cnt[value] over prefix values and a running answer. On add of
    #      prefix value pv: answer += cnt[pv ^ k]; cnt[pv] += 1. On remove:
    #      cnt[pv] -= 1; answer -= cnt[pv ^ k]. (Order matters — see SOLUTION.md.)
    #   5. Slide the two pointers to each window and store the answer.
    pass


if __name__ == "__main__":
    sample_a = [1, 2, 1, 1, 0, 3]
    sample_k = 3
    sample_queries = [(1, 6), (3, 5)]
    print(xor_favorite_number(sample_a, sample_k, sample_queries))
    # Expected: [7, 0]
