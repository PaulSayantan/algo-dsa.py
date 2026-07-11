# Count Distinct Palindromic Substrings

**Difficulty:** Medium

**Source:** Classic variant of LeetCode 647 / GeeksforGeeks "Count distinct
palindromic substrings"

## Description

Given a string `s`, return the number of **distinct** palindromic substrings of
`s`. Two palindromic substrings are considered the same if they are equal as
strings, regardless of where they occur. Unlike the position-based count, you
count each *unique palindrome content* only once.

For example, in `"aaa"` the palindromic substrings by position are
`"a", "a", "a", "aa", "aa", "aaa"`, but the **distinct** set is
`{"a", "aa", "aaa"}`, so the answer is `3`.

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Examples

**Example 1**

```
Input:  s = "aaa"
Output: 3
Explanation: The distinct palindromes are "a", "aa", "aaa".
```

**Example 2**

```
Input:  s = "abaaa"
Output: 5
Explanation: The distinct palindromes are "a", "b", "aba", "aa", "aaa".
             (Occurrences repeat, but each unique string is counted once.)
```

**Example 3**

```
Input:  s = "abc"
Output: 3
Explanation: The distinct palindromes are "a", "b", "c".
```

## Hint

Generate every palindromic substring with the **Longest Palindromic Substring
(expand around center)** technique — expand from all `2n - 1` centers — and add
each palindrome you discover to a set. The size of the set is the number of
distinct palindromes.
