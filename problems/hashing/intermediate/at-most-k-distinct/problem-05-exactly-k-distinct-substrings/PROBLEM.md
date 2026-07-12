# Count Substrings With Exactly K Distinct Characters

**Difficulty:** Medium

**Source:** Classic — exactly-K distinct characters (atMost difference)

## Description

Given a string `s` and an integer `k`, return the number of substrings of `s` that contain exactly `k` distinct characters. Apply the same `exactly(k) = atMost(k) - atMost(k-1)` identity, this time over characters.

## Examples

### Example 1

```
Input:  s = "pqpqs", k = 2
Output: 7
```

**Explanation:** The substrings with exactly 2 distinct chars: "pq","qp","pq","pqp","qpq","pqpq","qpqs"... 7 in total.

## Hint

Two character-window atMost passes; subtract. atMost(m<0) is 0.
