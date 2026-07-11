# Repeated Substring Pattern

**Difficulty:** Easy

**Source:** LeetCode 459 — "Repeated Substring Pattern"

## Description

Given a string `s`, return `true` if it can be constructed by taking a substring
of it and appending multiple copies of that substring together.

There is a neat reduction to a single substring search: `s` is a repetition of a
smaller block **iff** `s` appears inside `(s + s)` with its first and last
characters removed — i.e. inside `(s + s)[1 : -1]`. If a copy of `s` can be
found in that "doubled but trimmed" string, then `s` must be periodic with a
period smaller than its full length.

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "abab"
Output: true
Explanation: "abab" = "ab" + "ab". Equivalently, ("abab"+"abab")[1:-1] =
             "bababa", and "abab" appears inside it (at index 1).
```

### Example 2
```
Input:  s = "aba"
Output: false
Explanation: "aba" cannot be built by repeating a shorter block.
             ("aba"+"aba")[1:-1] = "baab", which does not contain "aba".
```

### Example 3
```
Input:  s = "abcabcabcabc"
Output: true
Explanation: It is "abc" repeated 4 times (also "abcabc" repeated twice).
```

## Hint

Search for `s` inside `(s + s)[1:-1]`; a hit means `s` is periodic. Do that
substring search with **Boyer–Moore (string search)**.
