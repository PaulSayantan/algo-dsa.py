# Count Distinct Substrings of Length L (Double Hash)

**Difficulty:** Medium

**Source:** Classic — double hashing

## Description

Given a string `s` and an integer `L`, count the number of distinct substrings of length exactly `L`, identifying each window by a **pair** of independent polynomial hashes so accidental collisions do not merge distinct substrings. Return `0` for an invalid `L`.

## Examples

### Example 1

```
Input:  s = "mississippi", L = 3
Output: 7
```

## Hint

Insert each window's (h1, h2) tuple into a set; the answer is the set's size.
