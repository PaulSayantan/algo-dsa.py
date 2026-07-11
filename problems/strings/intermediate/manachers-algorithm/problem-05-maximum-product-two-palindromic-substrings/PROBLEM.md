# Maximum Product of the Length of Two Palindromic Substrings

**Difficulty:** Hard

**Source:** LeetCode 1960 — Maximum Product of the Length of Two Palindromic Substrings

## Description

You are given a **0-indexed** string `s` of **odd** length `n`. You must choose
two **non-intersecting** substrings of `s`, both of **odd length**, such that both
are palindromes. Return the **maximum** possible product of the two substrings'
lengths.

Formally, choose four indices `i <= j < k <= l` such that both `s[i..j]` and
`s[k..l]` are palindromes of odd length, and return the maximum value of
`(j - i + 1) * (l - k + 1)`.

The two substrings must not overlap. Since every position must be coverable, both
chosen substrings have odd length and at least length 1, so a valid answer always
exists (product `>= 1`).

## Constraints

- `2 <= s.length <= 10^5`
- `s.length` is odd.
- `s` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "ababbb"
Output: 9
Explanation: Choose "aba" (length 3, indices 0..2) and "bbb" (length 3, indices
3..5). Both are odd-length palindromes and do not overlap. Product = 3 * 3 = 9.
```

### Example 2
```
Input:  s = "zaaaxbbby"
Output: 9
Explanation: Choose "aaa" (indices 1..3) and "bbb" (indices 5..7). Both are
odd-length palindromes and do not overlap. Product = 3 * 3 = 9.
```

### Example 3
```
Input:  s = "aba"
Output: 1
Explanation: The two substrings must not overlap, so each can only be a single
character, e.g. "a" (index 0) and "a" (index 2). Product = 1 * 1 = 1.
```

## Hint

Use **Manacher's Algorithm** (odd-length variant) to get every center's palindrome
radius, then build sweep arrays `left[i]` = best odd palindrome length ending at or
before `i`, and `right[i]` = best starting at or after `i`, so you can combine a
split point in O(1). Watch the "shrink" step that lets a long palindrome still
count as a shorter palindrome that fits within a boundary.
