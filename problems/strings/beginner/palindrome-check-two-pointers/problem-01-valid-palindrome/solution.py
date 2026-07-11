class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Return whether ``s`` is a palindrome, ignoring case and any
        characters that are not alphanumeric.

        Args:
            s: The input string, consisting of printable ASCII characters.

        Returns:
            True if the cleaned, lowercased string reads the same forwards
            and backwards; False otherwise.

        Example:
            >>> Solution().isPalindrome("A man, a plan, a canal: Panama")
            True
            >>> Solution().isPalindrome("race a car")
            False
        """
        # TODO: implement using two pointers moving inward.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # expected: True
    print(sol.isPalindrome("race a car"))                      # expected: False
    print(sol.isPalindrome(" "))                               # expected: True
