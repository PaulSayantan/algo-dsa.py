# Open the Lock

**Difficulty:** Medium

**Source:** LeetCode 752 — Open the Lock

## Description

A lock has 4 circular wheels, each showing a digit `0`-`9`. Each wheel wraps around (`9` -> `0` and `0` -> `9`). One move turns a single wheel by one slot. The lock starts at `'0000'`.

Given a list of `deadends` (states the lock must never enter) and a `target` state, return the minimum number of moves to reach `target` from `'0000'`, or `-1` if it is impossible.

Constraints: each state is a 4-character string of digits; `1 <= deadends.length <= 500`; `target` and `'0000'` are digit strings of length 4.

## Examples

### Example 1

```
Input:  deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
```

**Explanation:** A shortest sequence is `0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202`, avoiding every deadend.

## Hint

Treat each 4-digit state as a graph node with 8 neighbors (turn each wheel up/down); BFS the state space from `'0000'`, skipping deadends.
