"""Employee Free Time (LeetCode 759).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Interval:
    """A closed-open interval [start, end) as used by LeetCode 759."""

    def __init__(self, start: int = 0, end: int = 0) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:  # convenience for printing results
        return f"[{self.start}, {self.end}]"


class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        """Return the finite intervals of free time common to all employees.

        Args:
            schedule: A list of employees; each employee is a list of
                non-overlapping ``Interval`` busy periods sorted by start.

        Returns:
            A list of ``Interval`` objects, sorted by start, covering the maximal
            stretches during which no employee is busy (excluding the unbounded
            time before the first and after the last busy period).

        Example:
            >>> s = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]
            >>> Solution().employeeFreeTime(s)
            [[3, 4]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    sched1 = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]
    print(sol.employeeFreeTime(sched1))  # expected: [[3, 4]]

    sched2 = [
        [Interval(1, 3), Interval(6, 7)],
        [Interval(2, 4)],
        [Interval(2, 5), Interval(9, 12)],
    ]
    print(sol.employeeFreeTime(sched2))  # expected: [[5, 6], [7, 9]]

    sched3 = [[Interval(1, 4)], [Interval(2, 4)], [Interval(3, 4)], [Interval(5, 7)]]
    print(sol.employeeFreeTime(sched3))  # expected: [[4, 5]]
