# Shortest Distance to a Character

**Difficulty:** Easy

**Source:** LeetCode 821 — Shortest Distance to a Character

## Description

Given a string `s` and a character `c` that occurs in `s`, return an array `answer` where `answer[i]` is the distance from index `i` to the closest occurrence of `c`. Distance is `|i - j|` between indices.

## Examples

### Example 1

```
Input:  s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
```

## Hint

Two sweeps recording the most recent index of c: left-to-right, then right-to-left, taking the min.
