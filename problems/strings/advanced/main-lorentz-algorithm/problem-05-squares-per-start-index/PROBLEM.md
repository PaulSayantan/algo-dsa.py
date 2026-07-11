# Squares Starting at Each Index

**Difficulty:** Hard

Source: Classic Main–Lorentz application (per-position repetition profile).

## Description

A **tandem repeat** (**square**) is a substring of the form `XX`.

Given a string `s` of length `n`, return an integer array `ans` of length `n` where
`ans[i]` is the number of squares (counting different lengths separately) that
**start** at index `i`. In other words, `ans[i]` counts the number of block lengths
`L >= 1` for which `s[i : i+L] == s[i+L : i+2L]`.

## Constraints

- `1 <= len(s) <= 200_000`
- `s` consists of lowercase English letters.
- The sum of all entries can be Θ(n²), but each individual entry is at most `n/2`.

## Examples

### Example 1
```
Input:  s = "aaaa"
Output: [2, 1, 1, 0]
Explanation:
  index 0: "aa" (L=1) and "aaaa" (L=2)  -> 2 squares
  index 1: "aa" (L=1)                   -> 1 square
  index 2: "aa" (L=1)                   -> 1 square
  index 3: nothing fits                 -> 0 squares
```

### Example 2
```
Input:  s = "abcabcabc"
Output: [1, 1, 1, 1, 0, 0, 0, 0, 0]
Explanation: A length-6 square ("abcabc" style) starts at indices 0, 1, 2, and 3.
             No square starts at index 4 or later, and no other lengths qualify.
```

### Example 3
```
Input:  s = "mississippi"
Output: [0, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0]
Explanation: (letters: m i s s i s s i p p i)
  index 1: "ississ" = s[1:7], X = "iss"          -> 1 square
  index 2: "ss" = s[2:4], X = "s"; and
           "ssissi" = s[2:8], X = "ssi"          -> 2 squares
  index 5: "ss" = s[5:7], X = "s"                 -> 1 square
  index 8: "pp" = s[8:10], X = "p"                -> 1 square
  All other indices: 0.
```

## Hint

The **Main–Lorentz Algorithm** yields squares as O(n log n) contiguous start-index
ranges `[lo, hi]` for each length; add `+1` over each range with a **difference
array** and take a prefix sum to get every `ans[i]` at once.
