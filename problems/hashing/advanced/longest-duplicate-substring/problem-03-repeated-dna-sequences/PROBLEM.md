# Repeated DNA Sequences

**Difficulty:** Medium

**Source:** LeetCode 187 — Repeated DNA Sequences

## Description

The DNA sequence is a string over `A`, `C`, `G`, `T`. Given a string `s`, return **all** 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. Return them sorted; if there are none, return an empty list.

## Examples

### Example 1

```
Input:  s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGGTTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```

## Hint

Slide a length-10 window, count each window's occurrences, collect those seen twice; return sorted.
