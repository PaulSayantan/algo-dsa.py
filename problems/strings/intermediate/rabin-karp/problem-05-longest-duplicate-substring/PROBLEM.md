# Longest Duplicate Substring

**Difficulty:** Hard

**Source:** LeetCode 1044 — "Longest Duplicate Substring"

## Description

Given a string `s`, consider all its **duplicated substrings**: (contiguous)
substrings of `s` that occur two or more times. The occurrences **may overlap**.

Return **any** duplicated substring that has the **longest possible length**. If
`s` does not have a duplicated substring, return `""`.

This is the flagship Rabin–Karp problem. The answer length is **monotonic**: if
a duplicated substring of length `L` exists, then one of length `L-1` exists too
(any prefix of the duplicate). So we **binary search** on the length `L`, and for
each candidate `L` we ask "does some length-`L` substring appear twice?" — a
question answered in `O(n)` by hashing every length-`L` window with a rolling
hash and checking a set for repeats.

## Constraints

- `2 <= s.length <= 3 * 10^4`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "banana"
Output: "ana"
Explanation:
  "ana" occurs at index 1 and index 3 (the occurrences overlap).
  It has length 3; no duplicated substring of length 4 exists, so "ana" is longest.
```

### Example 2

```
Input:  s = "abcd"
Output: ""
Explanation:
  Every character is unique, so no substring occurs twice. The answer is "".
```

### Example 3

```
Input:  s = "aaaaa"
Output: "aaaa"
Explanation:
  "aaaa" occurs at index 0 and index 1 (overlapping). No length-5 substring
  repeats (there is only one), so the longest duplicate has length 4.
```

## Hint

The maximum duplicate length is **monotonic**, so **binary search** on the
length `L`. For each `L`, use **Rabin–Karp** with a rolling hash to test in
`O(n)` whether any length-`L` window repeats (store window hashes in a set).
