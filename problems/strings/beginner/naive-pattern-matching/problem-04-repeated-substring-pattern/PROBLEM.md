# Repeated Substring Pattern

**Difficulty:** Medium

**Source:** LeetCode 459 — Repeated Substring Pattern

## Description

Given a string `s`, check if it can be constructed by taking one of its **substrings**
and appending multiple copies of that substring together. Return `True` if it can,
otherwise `False`.

In other words, decide whether there is a substring `t` (with `1 <= len(t) < len(s)`)
such that `s` equals `t` repeated `k` times for some integer `k >= 2`.

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "abab"
Output: true
```

**Explanation:** `s` is `"ab"` repeated twice (`"ab" + "ab"`), so it can be built from a
repeated substring.

### Example 2

```
Input:  s = "aba"
Output: false
```

**Explanation:** No substring shorter than `"aba"` can be repeated a whole number of
times to form `"aba"` (`"a"` gives `"aaa"`, `"ab"` cannot tile length 3), so the answer
is `false`.

### Example 3

```
Input:  s = "abcabcabcabc"
Output: true
```

**Explanation:** `s` is `"abc"` repeated four times (it is also `"abcabc"` repeated
twice), so the answer is `true`.

## Hint

There is a neat reduction: build `doubled = s + s`, remove the first and last
characters, and check whether `s` appears inside that trimmed string. Perform that
substring search with **Naive Pattern Matching**. (Intuitively, if `s` is periodic it
"reappears" before shifting by a full copy.)

## Follow-up

Solving it directly is also fine: try each candidate period length `L` that divides
`len(s)`, and verify by naive matching that the block `s[0:L]` tiles the whole string.
