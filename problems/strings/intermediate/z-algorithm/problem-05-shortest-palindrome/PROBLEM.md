# Shortest Palindrome

**Difficulty:** Hard

**Source:** LeetCode 214 — "Shortest Palindrome".

## Description

You are given a string `s`. You may convert `s` into a palindrome by adding
characters **in front of it** (and only in front of it). Return the **shortest**
palindrome you can form this way.

The key sub-problem is: find the **longest prefix of `s` that is itself a
palindrome**. If that longest palindromic prefix has length `p`, then the
characters after it (`s[p:]`) must be mirrored and prepended, so the answer is
`reverse(s[p:]) + s`.

To find the longest palindromic prefix in linear time, build the combined string
`s + separator + reverse(s)` and compute its Z-array. For each index `i` in the
`reverse(s)` region, if the Z-match reaches all the way to the end of the
combined string (`z[i] == len(combined) - i`), then a prefix of `s` equals a
suffix of `reverse(s)` of that length — which is exactly a palindromic prefix of
`s`. The largest such length is `p`.

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "aacecaaa"
Output: "aaacecaaa"
Explanation: The longest palindromic prefix of "aacecaaa" is "aacecaa"
(length 7). The remaining suffix is "a"; reversing it gives "a", which we
prepend: "a" + "aacecaaa" = "aaacecaaa", a palindrome of length 9.
```

### Example 2

```
Input:  s = "abcd"
Output: "dcbabcd"
Explanation: The longest palindromic prefix of "abcd" is just "a" (length 1).
The remaining suffix is "bcd"; reversed it is "dcb", prepended:
"dcb" + "abcd" = "dcbabcd".
```

### Example 3

```
Input:  s = "aabba"
Output: "abbaabba"
Explanation: The longest palindromic prefix of "aabba" is "aa" (length 2). The
remaining suffix is "bba"; reversed it is "abb", prepended:
"abb" + "aabba" = "abbaabba", a palindrome of length 8.
```

## Hint

Compute the **Z-array** of `s + '#' + reverse(s)`. In the reversed region, a
Z-value that reaches the end of the combined string marks a palindromic prefix
of `s`; take the longest, then prepend the reverse of the leftover suffix.
