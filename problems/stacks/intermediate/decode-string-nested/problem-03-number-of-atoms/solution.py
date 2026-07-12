"""Number of Atoms — LeetCode 726."""


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # TODO: stack of count maps; '(' pushes a map, ')<mult>' pops and merges *mult
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countOfAtoms("H2O"))  # expected: 'H2O'
    print(sol.countOfAtoms("Mg(OH)2"))  # expected: 'H2MgO2'
    print(sol.countOfAtoms("K4(ON(SO3)2)2"))  # expected: 'K4N2O14S4'
    print(sol.countOfAtoms("(NB3)33"))  # expected: 'B99N33'
