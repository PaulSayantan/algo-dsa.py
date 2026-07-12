# Count Distinct Substrings of Length L

**Difficulty:** Medium

**Source:** Classic — distinct substrings via hashing

## Description

Given a string `s` and an integer `L`, count the number of **distinct** substrings of length exactly `L`. Hash every length-`L` window with prefix hashing and count distinct hash values. Return `0` if `L` is not a valid length.

## Examples

### Example 1

```
Input:  s = "banana", L = 2
Output: 3
```

**Explanation:** distinct: "ba", "an", "na"

## Hint

Add the hash of every window s[i:i+L] to a set; the answer is the set size.
