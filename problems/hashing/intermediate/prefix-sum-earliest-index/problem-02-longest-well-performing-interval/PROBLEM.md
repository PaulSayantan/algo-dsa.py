# Longest Well-Performing Interval

**Difficulty:** Medium

**Source:** LeetCode 1124 — Longest Well-Performing Interval

## Description

You are given `hours`, the hours worked per day. A day is *tiring* if hours > 8. A well-performing interval has strictly more tiring days than non-tiring days. Return the length of the longest such interval.

## Examples

### Example 1

```
Input:  hours = [9,9,6,0,6,6,9]
Output: 3
```

## Hint

tiring=+1 else -1. If prefix>0 whole prefix qualifies; else look for prefix-1 earliest.
