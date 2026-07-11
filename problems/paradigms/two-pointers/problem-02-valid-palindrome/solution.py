class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Return whether `s` is a palindrome ignoring case and non-alphanumerics.

        Only alphanumeric characters (letters and digits) are considered, and
        comparison is case-insensitive.

        Args:
            s: The input string of printable ASCII characters.

        Returns:
            True if the filtered, lowercased string reads the same forward and
            backward; otherwise False.

        Example:
            >>> Solution().isPalindrome("A man, a plan, a canal: Panama")
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # expected: True
    print(sol.isPalindrome("race a car"))                      # expected: False
    print(sol.isPalindrome(" "))                               # expected: True
