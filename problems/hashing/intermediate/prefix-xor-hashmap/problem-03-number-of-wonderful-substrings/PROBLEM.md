# Number of Wonderful Substrings

**Difficulty:** Medium

**Source:** LeetCode 1915 — Number of Wonderful Substrings

## Description

A string is **wonderful** if at most one of its letters appears an odd number of times. Given `word` consisting only of the letters `a`..`j`, return the number of wonderful non-empty substrings (counting each occurrence). Track a 10-bit parity bitmask prefix: a substring is wonderful iff the XOR of its endpoint masks is `0` (all even) or a single set bit (exactly one odd).

## Examples

### Example 1

```
Input:  word = "aba"
Output: 4
```

**Explanation:** The wonderful substrings are "a", "b", "a", "aba".

### Example 2

```
Input:  word = "aabb"
Output: 9
```

## Hint

For each prefix mask add count[mask] (all-even) plus count[mask ^ (1<<i)] for each of the 10 bits (one-odd).
