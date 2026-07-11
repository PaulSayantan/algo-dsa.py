# Distinct Echo Substrings

**Difficulty:** Hard

Source: LeetCode 1316 — "Distinct Echo Substrings".

## Description

Return the number of **distinct** non-empty substrings of `text` that can be
written as the concatenation of some string with itself — i.e. substrings of the
form `a + a` (a string `a` immediately followed by an identical copy).

Distinctness is by **content**: two occurrences of the same string count once. For
example, in `"leetcodeleetcode"` the substring `"ee"` appears twice but is counted
a single time.

## Constraints

- `1 <= len(text) <= 2000` (original LeetCode limit).
- Your Main–Lorentz solution should scale far beyond this — target `n` up to
  ~10⁵ for the enumeration, with hashing to deduplicate.
- `text` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  text = "abcabcabc"
Output: 3
Explanation: The distinct echo substrings are "abcabc", "bcabca", and "cabcab".
             Each is a string a + a with |a| = 3.
```

### Example 2
```
Input:  text = "leetcodeleetcode"
Output: 2
Explanation: The distinct echo substrings are "ee" (a = "e") and
             "leetcodeleetcode" (a = "leetcode"). Although "ee" occurs twice, it
             is counted once because we count distinct content.
```

### Example 3
```
Input:  text = "abcde"
Output: 0
Explanation: No substring is a concatenation of a string with itself.
```

## Hint

Enumerate all square occurrences in O(n log n) with the **Main–Lorentz Algorithm**,
then deduplicate by content using a rolling hash keyed on `(length, hash)` so that
equal substrings collapse to one.
