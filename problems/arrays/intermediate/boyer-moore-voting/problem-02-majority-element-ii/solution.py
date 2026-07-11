from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """Return every element that appears more than floor(n/3) times.

        At most two such elements can exist. Use the two-candidate extension of
        Boyer–Moore voting for the first pass, then verify each candidate with a
        second counting pass. Aim for O(n) time and O(1) extra space.

        Args:
            nums: A non-empty list of integers.

        Returns:
            A list of the (at most two) elements occurring more than
            len(nums) // 3 times, in any order.

        Example:
            >>> sorted(Solution().majorityElement([1, 2, 2, 3, 2, 1, 1]))
            [1, 2]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    print(s.majorityElement([3, 2, 3]))                 # expected: [3]
    print(s.majorityElement([1]))                       # expected: [1]
    print(s.majorityElement([1, 2, 2, 3, 2, 1, 1]))     # expected: [1, 2] (any order)
