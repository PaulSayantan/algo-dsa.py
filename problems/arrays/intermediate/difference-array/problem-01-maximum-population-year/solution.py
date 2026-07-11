from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """Return the earliest year with the maximum living population.

        A person with log [birth, death] is counted alive in every year x such
        that birth <= x < death (counted the birth year, not the death year).

        Args:
            logs: A list of [birth_year, death_year] pairs. Every year lies in
                the inclusive range [1950, 2050], and birth_year < death_year.

        Returns:
            The earliest calendar year that attains the maximum population.

        Example:
            >>> Solution().maximumPopulation([[1993, 1999], [2000, 2010]])
            1993
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumPopulation([[1993, 1999], [2000, 2010]]))          # expected: 1993
    print(sol.maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]))  # expected: 1960
