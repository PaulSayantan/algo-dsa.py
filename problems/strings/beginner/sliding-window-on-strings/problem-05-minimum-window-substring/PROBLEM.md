# Minimum Window Substring

**Difficulty:** Hard

**Source:** LeetCode 76 — Minimum Window Substring

## Description

Given two strings `s` and `t`, return the **shortest substring** of `s` that
contains every character of `t` (including duplicates). If no such substring
exists, return the empty string `""`.

"Contains every character of `t` including duplicates" means: for each distinct
character `c` in `t`, the window must contain at least as many copies of `c` as
`t` does. The characters do **not** need to appear in the same order as in `t`,
and the window may contain extra characters. The answer is guaranteed to be
unique when it exists.

## Constraints

- `1 <= len(s), len(t) <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Examples

### Example 1
```
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The window "BANC" (indices 9..12) contains one 'A', one 'B', and
             one 'C' — all of t. No shorter substring of s covers all three
             characters.
```

### Example 2
```
Input:  s = "a", t = "a"
Output: "a"
Explanation: The whole string is the smallest (and only) window that
             contains "a".
```

### Example 3
```
Input:  s = "a", t = "aa"
Output: ""
Explanation: t needs two 'a's but s has only one, so no window can cover t;
             the answer is the empty string.
```

## Hint

Use the **Sliding Window on Strings** technique with a "need vs have" match
counter: expand the window on the right until it covers all of `t`, then
contract from the left as far as possible while it still covers `t`, recording
the smallest covering window seen.
