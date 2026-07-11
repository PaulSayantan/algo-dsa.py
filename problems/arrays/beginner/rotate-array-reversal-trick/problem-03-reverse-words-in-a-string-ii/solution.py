from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """Reverse the order of the words in a character array, in place.

        Args:
            s: A list of single-character strings forming a sentence with words
               separated by single spaces and no leading/trailing spaces.
               Modified in place.

        Returns:
            None. The word order is reversed by mutating ``s`` directly.

        Example:
            >>> chars = list("the sky is blue")
            >>> Solution().reverseWords(chars)
            >>> "".join(chars)
            'blue is sky the'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    data = list("the sky is blue")
    Solution().reverseWords(data)
    print("".join(data))  # expected: 'blue is sky the'
