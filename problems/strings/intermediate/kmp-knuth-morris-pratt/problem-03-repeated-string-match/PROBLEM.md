# Repeated String Match

**Difficulty:** Medium

**Source:** LeetCode 686 — "Repeated String Match"

## Description

Given two strings `a` and `b`, return the **minimum number of times** you must
repeat string `a` so that `b` becomes a substring of the repeated string. If it
is impossible for `b` to ever be a substring no matter how many times `a` is
repeated, return `-1`.

For example, repeating `a = "abcd"` three times gives `"abcdabcdabcd"`, which
contains `b = "cdabcdab"` as a substring, so the answer is `3`.

## Constraints

- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  a = "abcd", b = "cdabcdab"
Output: 3
Explanation: Repeat a three times: "abcdabcdabcd".
             b = "cdabcdab" appears starting at index 2.
             Two copies "abcdabcd" are too short to contain b, so 3 is minimal.
```

### Example 2

```
Input:  a = "a", b = "aa"
Output: 2
Explanation: "a" repeated twice is "aa", which contains b. One copy is too short.
```

### Example 3

```
Input:  a = "abc", b = "cabcabca"
Output: 4
Explanation: "abc" * 4 = "abcabcabcabc" contains "cabcabca" at index 2.
             "abc" * 3 = "abcabcabc" (length 9) is too short to hold b (length 8)
             at the needed offset, so 4 copies are required.
```

## Hint

You only ever need `ceil(len(b)/len(a))` or one extra copy of `a`. Build that
bounded concatenation and run **KMP (Knuth–Morris–Pratt)** to test whether `b`
occurs, keeping the whole thing linear.
