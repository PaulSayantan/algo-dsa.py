"""Count Triplets That Can Form Two Arrays of Equal XOR — LeetCode 1442."""
from typing import List  # noqa: F401


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # TODO: XOR(i..j-1) == XOR(j..k) iff prefix[i] == prefix[k+1];
        #       each such (i, k) contributes (k - i) valid j split points.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countTriplets([2, 3, 1, 6, 7]))  # expected: 4
    print(sol.countTriplets([1, 1, 1, 1, 1]))  # expected: 10
    print(sol.countTriplets([2, 3]))  # expected: 0
    print(sol.countTriplets([5, 5]))  # expected: 1
    print(sol.countTriplets([1, 3, 5, 7, 9]))  # expected: 3
