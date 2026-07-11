# Repeated Substring Pattern

**Difficulty:** Easy

**Source:** LeetCode 459 — "Repeated Substring Pattern"

## Description

Given a string `s`, return `true` if it can be constructed by taking some
substring of it and appending multiple copies of that substring together.
Otherwise return `false`.

In other words, decide whether there exists a block `t` (with `len(t) < len(s)`)
such that `s = t + t + ... + t` (two or more copies). A single character string
cannot be built this way, since the block must be strictly shorter than `s`.

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "abab"
Output: true
Explanation: "abab" = "ab" + "ab", so the block "ab" repeated twice builds s.
```

### Example 2

```
Input:  s = "aba"
Output: false
Explanation: No block strictly shorter than "aba" repeats to form it.
             Length 3 is prime and s is not a single repeated character.
```

### Example 3

```
Input:  s = "abcabcabcabc"
Output: true
Explanation: The block "abc" repeated 4 times builds s
             (it is also "abcabc" repeated twice).
```

## Hint

Build the **LPS array** of `s`. The whole string is a repetition of a block iff
its smallest period `n - lps[n-1]` divides `n` and is smaller than `n`. This is
the periodicity property that falls straight out of **KMP (Knuth–Morris–Pratt)**.
