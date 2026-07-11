# Last Substring in Lexicographical Order

**Difficulty:** Hard

**Source:** LeetCode 1163 — "Last Substring in Lexicographical Order"

## Description

Given a string `s`, return the **last** substring of `s` in lexicographical order.

The lexicographically largest substring of a string is always one of its **suffixes**
(a larger prefix always beats its own prefix). So the task reduces to finding the
lexicographically **maximum suffix** of `s`.

## Constraints

- `1 <= s.length <= 4 * 10^5`
- `s` contains only lowercase English letters.

## Examples

### Example 1
```
Input:  s = "abab"
Output: "bab"
Explanation: The substrings starting with 'b' are "b" and "bab"; the largest is "bab".
             No substring starts with a letter greater than 'b', so "bab" is the answer.
```

### Example 2
```
Input:  s = "leetcode"
Output: "tcode"
Explanation: The maximum suffix is "tcode" (starting at the 't'); it beats "s"... there
             is no 's'; among suffixes it is the largest.
```

### Example 3
```
Input:  s = "banana"
Output: "nana"
Explanation: Suffixes starting with the largest letter 'n' are "nana" and "na"; the
             largest is "nana".
```

## Hint

This is the mirror of **Lyndon Factorization (Duval's algorithm)**: instead of finding
the minimum suffix (the last Lyndon factor), run the same two-pointer comparison but keep
the *larger* candidate. It finds the maximum suffix in `O(n)` time and `O(1)` space.
