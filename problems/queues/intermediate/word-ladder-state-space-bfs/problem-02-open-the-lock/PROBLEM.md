# Open the Lock

**Difficulty:** Medium

**Source:** LeetCode 752 — Open the Lock

## Description

A lock has 4 circular wheels, each showing a digit `0`-`9`. The wheels wrap around, so `9` can turn to `0` and `0` can turn to `9`. Each move turns exactly one wheel by one slot. The lock starts at `"0000"`.

Given a list of `deadends` (states the lock must never display) and a `target` string, return the minimum number of moves to reach `target`, or `-1` if it is impossible.

Constraints: each of `deadends` and `target` is a 4-character string of digits; `1 <= len(deadends) <= 500`.

## Examples

### Example 1

```
Input:  deadends=["0201","0101","0102","1212","2002"], target="0202"
Output: 6
```

**Explanation:** A shortest path is `0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202`.

## Hint

Each 4-digit combination is a state; neighbors differ by turning one wheel one slot (mod 10). BFS from `"0000"`, skipping deadends and visited states.
