"""Valid Palindrome — LeetCode 125.

Empty solution template. Fill in the body yourself.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Return True if `s` is a palindrome considering only alphanumeric
        characters and ignoring case.

        Args:
            s: A string of printable ASCII characters.

        Returns:
            True if the filtered, lowercased string reads the same forward and
            backward; False otherwise.

        Example:
            >>> Solution().isPalindrome("A man, a plan, a canal: Panama")
            True
        """
        # TODO: implement using two pointers (opposite ends)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # expected: True
    print(sol.isPalindrome("race a car"))                      # expected: False
    print(sol.isPalindrome(" "))                               # expected: True
