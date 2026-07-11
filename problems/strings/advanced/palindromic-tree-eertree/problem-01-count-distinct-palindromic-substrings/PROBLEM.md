# Count Distinct Palindromic Substrings

**Difficulty:** Medium

Source: Classic competitive-programming problem (SPOJ NUMOFPAL variant / GeeksforGeeks "Count distinct palindromic substrings"). Closely related to LeetCode 1930 "Unique Length-3 Palindromic Subsequences" but here we count *substrings* of any length.

## Description

Given a string `s`, count the number of **distinct** (unique) non-empty
substrings of `s` that are palindromes. A substring is a contiguous block of
characters. Two palindromic substrings are considered the same if they are equal
as strings, **regardless of how many times or where they occur**.

For example, in `"aba"` the palindromic substrings are `"a"` (occurs twice),
`"b"`, and `"aba"`. Even though `"a"` occurs twice, it is counted once, so the
answer is `3`.

Return the count of distinct palindromic substrings.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.
- A brute-force `O(n^2)` enumeration of substrings into a hash set is too slow
  and too memory-hungry near the upper bound; aim for an `O(n)`-node approach.

## Examples

### Example 1

```
Input:  s = "aba"
Output: 3
Explanation: The distinct palindromic substrings are "a", "b", and "aba".
             "a" appears twice but is counted only once.
```

### Example 2

```
Input:  s = "aabaa"
Output: 5
Explanation: The distinct palindromes are "a", "b", "aa", "aba", and "aabaa".
             That is 5 unique palindromic substrings.
```

### Example 3

```
Input:  s = "abc"
Output: 3
Explanation: No multi-character palindromes exist, so only the single letters
             "a", "b", and "c" count, giving 3.
```

## Hint

The number of *distinct* palindromic substrings of a string is exactly the
number of non-root nodes in its **Palindromic Tree (Eertree)** — because the
eertree creates exactly one node per distinct palindrome, and a string of
length `n` has at most `n` of them.
