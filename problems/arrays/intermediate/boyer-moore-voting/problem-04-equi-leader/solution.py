from typing import List


class Solution:
    def equiLeaders(self, A: List[int]) -> int:
        """Count the equi leaders of the array A.

        An index S (0 <= S < N-1) is an equi leader if the prefix A[0..S] and
        the suffix A[S+1..N-1] have the same leader (strict majority value).
        The shared value must be the leader of the whole array, so find that
        global leader with Boyer–Moore voting (verify it), then sweep every
        split comparing prefix counts to each half's majority threshold. Aim
        for O(N) time and O(1) extra space.

        Args:
            A: A non-empty list of integers.

        Returns:
            The number of equi-leader split points.

        Example:
            >>> Solution().equiLeaders([4, 3, 4, 4, 4, 2])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    print(s.equiLeaders([4, 3, 4, 4, 4, 2]))    # expected: 2
    print(s.equiLeaders([1, 1, 1, 1]))          # expected: 3
    print(s.equiLeaders([1, 2, 3]))             # expected: 0
