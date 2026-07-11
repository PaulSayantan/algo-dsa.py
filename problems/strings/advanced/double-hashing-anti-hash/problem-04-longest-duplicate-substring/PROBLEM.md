# Longest Duplicate Substring

**Difficulty:** Hard

**Source:** LeetCode 1044 — Longest Duplicate Substring

## Description

Given a string `s`, consider all of its **duplicated substrings**: (contiguous)
substrings of `s` that occur **two or more times**. The occurrences may overlap.

Return **any** duplicated substring that has the **longest possible length**. If
`s` has no duplicated substring, return `""`.

The key observation is monotonic: if a duplicated substring of length `L`
exists, then one of length `L-1` exists too (any prefix of it is also
duplicated). So we can **binary search** the answer length `L`, and for each
candidate `L` ask "is there a repeated substring of length `L`?" That existence
check is done by hashing every length-`L` window and looking for a collision in
a hash set — which is exactly where **double hashing** protects us from false
positives that would otherwise report a duplicate that is not real.

## Constraints

- `2 <= s.length <= 3 * 10^4`
- `s` consists of lowercase English letters.

## Examples

**Example 1**

```
Input:  s = "banana"
Output: "ana"
Explanation: "ana" occurs at index 1 and index 3 (overlapping). No duplicated
substring of length 4 exists, so length 3 is the maximum.
```

**Example 2**

```
Input:  s = "abcd"
Output: ""
Explanation: No substring occurs more than once, so the answer is the empty
string.
```

**Example 3**

```
Input:  s = "aaaaa"
Output: "aaaa"
Explanation: "aaaa" occurs at index 0 and index 1 (overlapping). Length 5 would
be the whole string, which occurs only once, so 4 is the maximum.
```

## Hint

Use **Double Hashing / Anti-Hash**: binary search the length `L`; for each `L`,
roll a two-modulus hash over all windows of length `L` and detect a repeat via a
hash set. Two moduli keep the "duplicate found" decision from being fooled by a
collision.
