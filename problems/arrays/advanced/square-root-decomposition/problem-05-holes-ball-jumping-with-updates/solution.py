"""Holes — Ball Jumping with Power Updates (Codeforces 13E, 0-indexed).

Empty solution template. Fill in the body yourself using Square Root
Decomposition (block "escape" precomputation and block-to-block hops).
"""

from typing import List


class Holes:
    def __init__(self, powers: List[int]) -> None:
        """Initialize the row of holes.

        Args:
            powers: Positive jump powers, one per hole (0-indexed).

        Example:
            >>> h = Holes([2, 1, 1, 3, 1, 2])
            >>> h.throw(0)
            [3, 3]
        """
        # TODO: implement — block size ~ sqrt(n); per-hole (jumps_to_leave_block,
        #                    hole_after_block, last_hole_in_block)
        pass

    def set_power(self, index: int, val: int) -> None:
        """Set ``powers[index] = val`` and recompute the affected block.

        Args:
            index: The hole whose power changes (0-indexed).
            val: The new positive power for that hole.

        Returns:
            None. Mutates internal state in place.
        """
        # TODO: implement — recompute the single block containing ``index``
        #                    from right to left
        pass

    def throw(self, start: int) -> List[int]:
        """Throw a ball into hole ``start`` and report where it ends.

        Args:
            start: The hole the ball is thrown into (0-indexed).

        Returns:
            A list ``[last_hole, num_jumps]``: the last hole occupied before the
            ball leaves the row, and the total number of jumps made.
        """
        # TODO: implement — hop block-to-block using the precomputed escapes
        pass


if __name__ == "__main__":
    h = Holes([2, 1, 1, 3, 1, 2])
    print(h.throw(0))      # expected: [3, 3]
    h.set_power(2, 4)
    print(h.throw(0))      # expected: [2, 2]

    h2 = Holes([1, 1, 1, 1, 1])
    print(h2.throw(0))     # expected: [4, 5]
    print(h2.throw(2))     # expected: [4, 3]
    h2.set_power(1, 10)
    print(h2.throw(0))     # expected: [1, 2]
