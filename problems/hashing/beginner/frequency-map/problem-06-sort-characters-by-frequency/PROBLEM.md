# Sort Characters By Frequency

**Difficulty:** Medium

**Source:** LeetCode 451 — Sort Characters By Frequency

## Description

Given a string `s`, return a string with the characters sorted in **decreasing order of frequency**: a character that occurs more often comes first, and each character is repeated as many times as it occurs. (The test inputs here have all-distinct frequencies, so the ordering is unique.)

## Examples

### Example 1

```
Input:  s = "aaabbc"
Output: "aaabbc"
```

**Explanation:** 'a' x3, 'b' x2, 'c' x1.

## Hint

Count characters, order them by descending count, and concatenate each character repeated its count.
