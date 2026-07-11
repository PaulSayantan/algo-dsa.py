# Lyndon Factorization of a String

**Difficulty:** Medium

**Source:** Classic (Chen–Fox–Lyndon theorem; Duval 1983). Appears as CSES / SPOJ-style string tasks.

## Description

By the **Chen–Fox–Lyndon theorem**, every non-empty string `s` can be written uniquely
as a concatenation of Lyndon words in **non-increasing** order:

```
s = w1 + w2 + ... + wk   with   w1 >= w2 >= ... >= wk   (lexicographically)
```

where each `wi` is a Lyndon word (strictly smaller than all of its proper suffixes).

Given `s`, return this list of factors `[w1, w2, ..., wk]` in order.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "banana"
Output: ["b", "an", "an", "a"]
Explanation: "b" >= "an" >= "an" >= "a" and each piece is a Lyndon word.
             Concatenated they give back "banana".
```

### Example 2
```
Input:  s = "abacaba"
Output: ["abac", "ab", "a"]
Explanation: "abac" >= "ab" >= "a"; each is Lyndon and the concatenation is "abacaba".
```

### Example 3
```
Input:  s = "aaa"
Output: ["a", "a", "a"]
Explanation: The only Lyndon word using just 'a' is "a" itself, so the factorization is
             three copies of "a" (equal factors are allowed since the order is
             non-increasing, i.e. "a" >= "a" >= "a").
```

## Hint

This is precisely what **Lyndon Factorization (Duval's algorithm)** computes in `O(n)`
time and `O(1)` extra space, using a three-pointer scan (`i`, `j`, `k`).
