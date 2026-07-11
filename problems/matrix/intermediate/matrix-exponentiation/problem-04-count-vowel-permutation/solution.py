"""Count Vowel Permutation (LeetCode 1220), large-n variant, modulo 1e9+7.

Fill in the body using Matrix Exponentiation on a 5x5 transition matrix so it
runs in O(log n). Do NOT use an O(n) loop — n can be as large as 10**18.
"""

MOD = 10**9 + 7


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """Return the number of valid length-n vowel strings, modulo 1e9+7.

        Rules: 'a'->'e'; 'e'->'a'|'i'; 'i'->any vowel except 'i';
        'o'->'i'|'u'; 'u'->'a'.

        Args:
            n: Desired string length, 1 <= n <= 10**18.

        Returns:
            Count of valid strings of length n, modulo 10**9 + 7.

        Example:
            >>> Solution().countVowelPermutation(2)
            10
        """
        # TODO: implement using matrix exponentiation.
        #   State = counts of strings ending in [a, e, i, o, u].
        #   Build the 5x5 transition matrix, raise it to the (n-1)-th power,
        #   apply it to the all-ones initial vector, and sum the entries.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countVowelPermutation(1))  # expected: 5
    print(sol.countVowelPermutation(2))  # expected: 10
    print(sol.countVowelPermutation(5))  # expected: 68
