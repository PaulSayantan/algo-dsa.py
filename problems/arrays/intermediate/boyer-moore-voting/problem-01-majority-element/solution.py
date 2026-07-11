from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Return the element that appears more than floor(n/2) times.

        The majority element is guaranteed to exist, so a single Boyer–Moore
        voting pass suffices (no verification pass needed). Aim for O(n) time
        and O(1) extra space.

        Args:
            nums: A non-empty list of integers containing a strict majority
                element (one appearing more than len(nums) // 2 times).

        Returns:
            The majority element.

        Example:
            >>> Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    print(s.majorityElement([3, 2, 3]))                 # expected: 3
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))     # expected: 2
    print(s.majorityElement([7]))                       # expected: 7
