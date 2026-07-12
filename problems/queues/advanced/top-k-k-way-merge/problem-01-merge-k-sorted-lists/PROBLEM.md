# Merge k Sorted Lists

**Difficulty:** Hard

**Source:** LeetCode 23 — Merge k Sorted Lists

## Description

Given `lists`, an array of `k` already-ascending integer lists, merge them into a single sorted list and return it. (Here lists are plain Python lists rather than linked lists.)

## Examples

### Example 1

```
Input:  lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

## Hint

Push each list's head (value, list index, elem index) into a min-heap; pop and push the next from that list.
