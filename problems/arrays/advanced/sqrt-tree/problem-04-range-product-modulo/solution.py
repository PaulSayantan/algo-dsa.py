"""Range Product Modulo m via a Sqrt Tree.

The op is (x, y) -> (x * y) % m, which is associative but NOT invertible and
NOT idempotent, so prefix products and sparse tables both fail.

Fill in the implementation. Do NOT hard-code answers.
"""
from typing import List


class RangeProductMod:
    """O(1) range-product-mod-m queries on a static array using a Sqrt Tree.

    Example:
        >>> rp = RangeProductMod([3, 7, 4, 9, 6, 2], 100)
        >>> rp.query(0, 2)     # 3*7*4 = 84
        84
        >>> rp.query(2, 5)     # 4*9*6*2 = 432 -> 32
        32
    """

    def __init__(self, nums: List[int], mod: int) -> None:
        """Preprocess `nums` so range products mod `mod` can be answered in O(1).

        Args:
            nums: Static array of non-negative integers, length n (1 <= n <= 1e5),
                  each already reduced so that 0 <= nums[i] < mod.
            mod:  The modulus m (2 <= m <= 1e9), not necessarily prime.

        Build target: O(n log log n) time and space. Use op = (x, y) -> x*y % mod.
        Do NOT try prefix products with modular inverse; mod may be composite and
        elements may share factors with mod, so inverses need not exist.
        """
        # TODO: implement
        pass

    def query(self, l: int, r: int) -> int:
        """Return (nums[l] * ... * nums[r]) mod m.

        Args:
            l: Left index, 0 <= l <= r.
            r: Right index, r < n.

        Returns:
            The product of nums[l..r] taken modulo m.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    rp = RangeProductMod([3, 7, 4, 9, 6, 2], 100)
    print(rp.query(0, 2))  # expected: 84
    print(rp.query(2, 5))  # expected: 32
    print(rp.query(1, 3))  # expected: 52
    print(rp.query(0, 5))  # expected: 72
