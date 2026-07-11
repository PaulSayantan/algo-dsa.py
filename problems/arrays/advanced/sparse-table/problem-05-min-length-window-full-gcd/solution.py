"""Number of Operations to Make GCD Array Uniform (Codeforces 1547F).

Approach to implement:
  1. Compute G = gcd of the whole array.
  2. Duplicate the array (a + a) so cyclic windows become plain subarrays.
  3. Build a Sparse Table over gcd (idempotent).
  4. For each start i in [0, n), binary-search the shortest window length L
     such that gcd(doubled[i .. i + L - 1]) == G.
  5. Answer = (max over starts of L) - 1.
"""

from typing import List


class Solution:
    def min_operations_to_uniform_gcd(self, a: List[int]) -> int:
        """Return the minimum number of neighbor-gcd operations to equalize a.

        Each operation replaces every element with gcd(a[i], a[(i+1) % n])
        simultaneously. The answer is the smallest k for which all elements
        become equal (they all become the array-wide gcd G).

        Args:
            a: A cyclic array of positive integers.

        Returns:
            The minimum number of operations needed to make all elements equal.

        Example:
            >>> Solution().min_operations_to_uniform_gcd([16, 24, 10, 5])
            3
            >>> Solution().min_operations_to_uniform_gcd([42, 42, 42, 42])
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().min_operations_to_uniform_gcd([16, 24, 10, 5]))   # Expected: 3
    print(Solution().min_operations_to_uniform_gcd([42, 42, 42, 42]))  # Expected: 0
    print(Solution().min_operations_to_uniform_gcd([4, 6, 4]))         # Expected: 2
    print(Solution().min_operations_to_uniform_gcd([1, 2, 3, 4, 5]))   # Expected: 1
