"""Range Affine (Linear Function) Composition via a Sqrt Tree.

Each element is a pair (a, b) representing f(x) = a*x + b (mod M).
The op is affine composition, which is associative but NON-commutative
and non-invertible for prefix arrays -- so neither prefix combination nor a
sparse table works, and the Sqrt Tree is the idiomatic O(1)-query structure.

Fill in the implementation. Do NOT hard-code answers.
"""
from typing import List, Tuple

MOD = 1_000_000_007


class RangeAffine:
    """O(1) range affine-composition queries via a Sqrt Tree.

    Element i is (a_i, b_i) meaning f_i(x) = a_i*x + b_i (mod MOD).
    query(l, r, x) returns f_l(f_{l+1}(...f_r(x)...)) mod MOD.

    Example:
        >>> ra = RangeAffine([(2, 3), (1, 5), (3, 0), (2, 1)])
        >>> ra.query(1, 2, 2)     # f1(f2(2)) = f1(6) = 11
        11
        >>> ra.query(0, 3, 1)     # 31
        31
    """

    def __init__(self, funcs: List[Tuple[int, int]]) -> None:
        """Preprocess the list of affine maps for O(1) range composition.

        Args:
            funcs: List of (a_i, b_i) pairs, length n (1 <= n <= 1e5), each with
                   0 <= a_i, b_i < MOD.

        Build target: O(n log log n) time and space. Use the composition op
            op((a1, b1), (a2, b2)) = (a1*a2 % MOD, (a1*b2 + b1) % MOD)
        where the FIRST argument is the outer (smaller-index) function. Because
        composition is not commutative, the argument order in every combine must
        keep outer-on-the-left.
        """
        # TODO: implement
        pass

    def query(self, l: int, r: int, x: int) -> int:
        """Return f_l(f_{l+1}(...f_r(x)...)) mod MOD.

        Args:
            l: Left (outermost) index, 0 <= l <= r.
            r: Right (innermost) index, r < n.
            x: The value to evaluate the composed function at, 0 <= x < MOD.

        Returns:
            The composed affine map over [l, r] applied to x, taken mod MOD.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    ra = RangeAffine([(2, 3), (1, 5), (3, 0), (2, 1)])
    print(ra.query(1, 2, 2))  # expected: 11
    print(ra.query(0, 3, 1))  # expected: 31
    print(ra.query(0, 1, 0))  # expected: 13  (f1(0)=5; f0(5)=2*5+3=13)
