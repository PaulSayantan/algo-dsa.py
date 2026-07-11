"""Gas Station — LeetCode 134.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Return a valid starting station index, or -1 if none exists.

        Stations are arranged in a circle. Starting with an empty tank at some
        station, you must be able to drive clockwise once around the whole circuit.

        Args:
            gas: gas[i] is the fuel available at station i.
            cost: cost[i] is the fuel needed to go from station i to station i+1.

        Returns:
            The unique starting index if the circuit can be completed, else -1.

        Example:
            >>> Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
            3
            >>> Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3])
            -1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # expected: 3
    print(sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))              # expected: -1
    print(sol.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))  # expected: 4
