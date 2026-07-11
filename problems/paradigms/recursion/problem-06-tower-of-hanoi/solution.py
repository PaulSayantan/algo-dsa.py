"""Tower of Hanoi — classic recursion problem.

Empty solution template. Fill in the body yourself using Recursion.
"""
from typing import List, Tuple


class Solution:
    def towerOfHanoi(
        self,
        n: int,
        source: str = "A",
        auxiliary: str = "B",
        target: str = "C",
    ) -> List[Tuple[str, str]]:
        """Return the sequence of moves to shift n disks from source to target.

        Move all n disks from `source` to `target` using `auxiliary`, moving one
        disk at a time and never placing a larger disk on a smaller one. Solve it
        with Recursion: move n-1 disks to the auxiliary peg, move the largest disk
        to the target, then move the n-1 disks onto the target. Base case: n == 0
        contributes no moves.

        Args:
            n: The number of disks to move (1 <= n <= 20).
            source: Label of the peg the disks start on.
            auxiliary: Label of the spare peg.
            target: Label of the peg the disks must end on.

        Returns:
            A list of (from_peg, to_peg) moves in the order to perform them.
            The optimal solution has exactly 2**n - 1 moves.

        Example:
            >>> Solution().towerOfHanoi(2)
            [('A', 'B'), ('A', 'C'), ('B', 'C')]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.towerOfHanoi(1))  # expected: [('A', 'C')]
    print(sol.towerOfHanoi(2))  # expected: [('A', 'B'), ('A', 'C'), ('B', 'C')]
    print(sol.towerOfHanoi(3))
    # expected: [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'),
    #            ('B', 'A'), ('B', 'C'), ('A', 'C')]
