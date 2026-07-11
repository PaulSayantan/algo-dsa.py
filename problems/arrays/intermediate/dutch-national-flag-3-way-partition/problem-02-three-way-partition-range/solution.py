from typing import List


class Solution:
    def threeWayPartition(
        self, arr: List[int], lowVal: int, highVal: int
    ) -> List[int]:
        """Partition ``arr`` in place around the range [lowVal, highVal].

        After partitioning, all elements < lowVal appear first, then all
        elements in [lowVal, highVal], then all elements > highVal. Relative
        order within each region does not matter. Target a single pass with
        O(1) extra space (Dutch National Flag with a range pivot).

        Args:
            arr: The list of integers to partition (mutated in place).
            lowVal: Lower bound of the inclusive middle range.
            highVal: Upper bound of the inclusive middle range (>= lowVal).

        Returns:
            The same list object, partitioned in place.

        Example:
            >>> Solution().threeWayPartition([1, 4, 2, -2, 5, 8, 0], 2, 5)
            [1, 0, -2, 2, 4, 5, 8]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    a = [1, 4, 2, -2, 5, 8, 0]
    print(s.threeWayPartition(a, 2, 5))
    # expected: elements < 2 first, then [2,5], then > 5
    # e.g. [1, 0, -2, 2, 4, 5, 8]

    b = [7, 7, 7]
    print(s.threeWayPartition(b, 1, 3))
    # expected: [7, 7, 7]  (all > highVal)
