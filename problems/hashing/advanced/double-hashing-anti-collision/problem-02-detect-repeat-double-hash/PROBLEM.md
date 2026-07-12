# Detect a Repeated Substring of Length L (Double Hash)

**Difficulty:** Medium

**Source:** Classic — double hashing

## Description

Given a string `s` and an integer `L`, determine whether **any** substring of length `L` occurs at least twice, using double hashing to compare windows robustly. Return a boolean (`False` for an invalid `L`).

## Examples

### Example 1

```
Input:  s = "banana", L = 2
Output: True
```

**Explanation:** "an"/"na" repeat

## Hint

Stream window keys into a set; report True the first time a key reappears.
